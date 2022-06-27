# import asyncio
#
# import aiohttp
#
#
# async def async_main():
#     async with aiohttp.ClientSession() as session:
#         for i in range(100):
#             # url = "https://coinmap.org/api/v1/venues/"
#             # url = "https://google.com"
#             url = "https://coinmap.org/api/v1/venues/"
#
#             await session.get(url)
#             print(f"Request {i + 1} is done!")
#
# async def main():
#     await async_main()
#
# if __name__=='__main__':
#     asyncio.run(main())
import asyncio
from functools import wraps
import aiohttp


async def request(session, i):
    print(f'done {i}')
    url = "https://coinmap.org/api/v1/venues/"
    await session.get(url)
    print(f'DONE {i}')



async def main():
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*(request(session, i)
                               for i in range(10)))
if __name__=='__main__':
     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
     asyncio.run(main())
