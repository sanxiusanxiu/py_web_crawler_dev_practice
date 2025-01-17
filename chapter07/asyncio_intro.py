import asyncio  # 引入asyncio才能使用关键字async await

def asyncio_intro01():
    # 定义一个execute()方法
    async def execute(x):
        print('execute:', x)

    '''
    coroutine：在Python中常指代协程对象类型，我们可以将协程对象注册到事件循环中，它会被事件循环调用
      我们可以使用async关键字来定义一个方法，这个方法在调用时不会立即被执行，而是会返回一个协程对象

    event_loop：事件循环，相当于一个无限循环，我们可以把一些函数注册到这个事件循环上，当满足发生条件的时候，就调用对应的处理方法

    task：任务，这是对协程对象的进一步封装，包含协程对象的各个状态
    future：代表将来执行或者没有执行的任务的结果，实际上和task没有本质区别
    '''
    # 直接调用后并不会执行，而是返回一个coroutine对象
    coroutine = execute(1)
    print('coroutine:', coroutine)

    # 创建一个事件循环loop
    loop = asyncio.get_event_loop()
    # 将协程对象注册到事件循环中
    loop.run_until_complete(coroutine)
    print('loop')


def asyncio_intro02():
    # 随着Python的更新，intro01中的写法已经不再使用

    # 定义一个execute()方法
    async def execute(x):
        print('execute:', x)

    # 使用asyncio.run()来运行协程
    asyncio.run(execute(1))

    # 这行代码将在协程执行完毕后执行
    print('loop')


def asyncio_intro03():
    # 定义一个execute()方法
    async def execute(x):
        print('execute:', x)
        return x

    # 直接调用后并不会执行，而是返回一个coroutine对象
    coroutine = execute(1)
    print('coroutine:', coroutine)

    # 创建一个事件循环loop
    loop = asyncio.get_event_loop()
    # 将协程对象转化为task对象
    task = loop.create_task(coroutine)
    print('task1:', task)
    # 将task对象注册到事件循环中
    loop.run_until_complete(task)
    print('task2:', task)
    print('loop')


def asyncio_intro04():
    # 定义一个execute()方法
    async def execute(x):
        print('execute:', x)
        return x

    # 直接调用后并不会执行，而是返回一个coroutine对象
    coroutine = execute(1)
    print('coroutine:', coroutine)

    # 定义task对象
    task = asyncio.ensure_future(coroutine)
    # 创建一个事件循环loop
    loop = asyncio.get_event_loop()
    # 将task对象注册到事件循环中
    loop.run_until_complete(task)
    print('task:', task)
    print('loop')


# asyncio_intro01()
