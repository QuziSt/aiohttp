import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession as session:
        response = await session.post(
            'http"//127.0.0.1:8080/users/',
            json={
                'name': 'John',
                'password': '1234'
                }
        )
        
asyncio.run(main())