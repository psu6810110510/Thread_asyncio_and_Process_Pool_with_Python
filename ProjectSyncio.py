import asyncio
import aiohttp
import time

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def get_data_async(num):
    url = "http://localhost:5000/api/data"
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for _ in range(num)]
        await asyncio.gather(*tasks)

start = time.time()
asyncio.run(get_data_async(10))
end = time.time()
print(f"Time taken (Asyncio): {end - start:.4f} seconds")