import asyncio

import aiohttp

name_of_dishes = ['salad', 'soup','борщ']
time_to_cook = [10, 20, 12]


async def waiter(args):
    list_of_orders = []

    list_of_orders.append(args)
    index_dish = name_of_dishes.index(args)
    time = 0
    time += time_to_cook[index_dish]
    print('заказ принят')
    await cook(list_of_orders, time_to_cook)
    print(f'{list_of_orders} передано на готовку, время готовки {time}')


async def cook(args, time):
    print(f'заказ {args} готовится')
    await asyncio.sleep(3)
    print('заказ готов')


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(waiter('salad'))

#
# async def main(*args, n):
#     waiter(*args,n)
