from aiohttp import web
from server import app, UserView

app.add_routes([
 web.post('/users/', UserView),
 web.get('/users/{user_id:\d+}', UserView),
 web.patch('/users/{user_id:\d+}', UserView),
 web.delete('/users/{user_id:\d+}', UserView) 
])