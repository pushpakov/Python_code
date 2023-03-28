import asyncio

# Defining coroutines
async def coro1():
    print('Coro1 starting')
    await asyncio.sleep(1)
    print('Coro1 ending')

async def coro2():
    print('Coro2 starting')
    await asyncio.sleep(2)
    print('Coro2 ending')
    raise ValueError('Something went wrong')

async def slow_operation():
    print('Starting slow operation')
    await asyncio.sleep(5)
    print('Slow operation complete')
    return 'Done'

async def fast_operation():
    print('Starting fast operation')
    await asyncio.sleep(1)
    print('Fast operation complete')
    return 'Done'

# Define main coroutine
async def main():
    print('Starting event loop')

    # Create tasks using create_task()
    task1 = asyncio.create_task(coro1())
    task2 = asyncio.create_task(coro2())
    task3 = asyncio.create_task(slow_operation())
    task4 = asyncio.create_task(fast_operation())

    try:
        # Wait for tasks to complete using gather()
        await asyncio.gather(task1, task2, task3, task4)
    except Exception as e:
        # Handle any exceptions raised by coroutines
        print(f'Caught exception: {e}')

    # Event loop finished
    print('Event loop finished')

# Start event loop using asyncio.run()
asyncio.run(main())
