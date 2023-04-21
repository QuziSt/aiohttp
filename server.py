import json
from aiohttp import web
from sqlalchemy.exc import IntegrityError
from bcrypt import hashpw, gensalt, checkpw
from models import Session, orm_context, User


@web.middleware
async def session_middleware(request, handler):
    async with Session() as session:
        request['session'] = session
        response = await handler(request)
        return response


app = web.Application()
app.cleanup_ctx(orm_context)
app.middlewares.append(session_middleware)


def hash_password(password):
    password = password.encode()
    password = hashpw(password, salt=gensalt())
    password = password.decode()
    return password
    


class UserView(web.View):
    async def get(self):
        pass
    
    async def post(self):
        json_data = self.request.json()
        json_data['password'] = hash_password(json_data['password'])
        user = User(**json_data)
        self.request['session'].add(user)
        try:
            await self.request['session'].commit()
        except IntegrityError as err:
            raise web.HTTPConflict(
                text=json.dumps({'error': 'user already exists'}),
                content_type='application/json'
            )
        return web.json_response({
            'id':user.id,
            'username': user.username,
            'email': user.email
            })
    
    async def patch(self):
        pass
    
    async def delete(self):
        pass


if '__main__' == __name__:
    web.run_app(app)