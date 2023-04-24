import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        response = await session.post('http://127.0.0.1:8080/posts/',
                                      json={
                                          'creator': 1,
                                          'post_header': ' мой',
                                          'post_text': ' текст',
                                          
                                      })
        data = await response.json()
        print(data)
        
    # async with aiohttp.ClientSession() as session:
    #     response = await session.post('http://127.0.0.1:8080/users/',
    #                                   json={
    #                                       'username': 'Hulk',
    #                                       'password': 'NewPass',
    #                                       'email': '123123123123'
    #                                   })
    #     data = await response.json()
    #     print(data)
        
asyncio.run(main())