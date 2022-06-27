# import asyncio
# import aiohttp
# from codetiming import Timer
#
#
# async def task(name, work_queue):
#     timer = Timer(text=f"Task {name} ellapsed time {{:.1f}}")
#     async with aiohttp.ClientSession() as session:
#         while not work_queue.empty():
#             url = await work_queue.get()
#             print(f" Task {name} getting {url}")
#             timer.start()
#             async with session.get(url) as response:
#                 await response.text()
#             timer.stop()
#
#
# async def main():
#     work_queue = asyncio.Queue()
#     for url in [
#         "http://google.com",
#         "http://linkedin.com",
#     ]:
#         await work_queue.put(url)
#
#     with Timer(f"Text total ellapsed {{:.1f}}"):
#         await asyncio.gather(
#             asyncio.create_task(task("One", work_queue)),
#             asyncio.create_task(task("Two", work_queue))
#         )
#
# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# asyncio.run(main())

import asyncio
import aiohttp
from codetiming import Timer


async def task(name, work_queue):
    timer = Timer(text=f"Task {name} ellapsed time {{:.1f}}")
    async with aiohttp.ClientSession() as session:
        while not work_queue.empty():
            url = await work_queue.get()
            print(f" Task {name} getting {url}")
            timer.start()
            async with session.get(url) as response:
                await response.text()
            timer.stop()




async def main():
    work_queue = asyncio.Queue()
    for url in [
        "http://google.com",
        "http://linkedin.com",
        "https://fastapi.tiangolo.com/advanced/sql-databases-peewee/"
    ]:
        await work_queue.put(url)

    with Timer(text="\nText total ellapsed {:.1f}"):
        await asyncio.gather(
            asyncio.create_task(task("One", work_queue)),
            asyncio.create_task(task("Two", work_queue)),
            asyncio.create_task(task("Three", work_queue))
        )


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())

