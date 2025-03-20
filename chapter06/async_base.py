import asyncio  # 引入 asyncio 才能使用关键字 async、await

def async_intro01():
    # 定义一个 execute() 方法
    async def execute(x):
        print('执行：', x)

    # 直接调用后并不会执行，而是返回一个 coroutine 对象
    coroutine = execute(1)
    print('coroutine 对象:', coroutine)

    # 创建一个事件循环 loop
    loop = asyncio.get_event_loop()
    # 将协程对象注册到事件循环中
    loop.run_until_complete(coroutine)
    print('事件循环 loop')

    # coroutine 对象: <coroutine object async_intro01.<locals>.execute at 0x000001693DE33510>
    # 执行： 1
    # 事件循环 loop

    """
    coroutine：在 Python 中常指代协程对象类型，我们可以将协程对象注册到事件循环中，它会被事件循环调用。可以使用 async 关键字来定义一个方法，这个方法在调用时不会立即被执行，而是会返回一个协程对象
    event_loop：事件循环，相当于一个无限循环，我们可以把一些函数注册到这个事件循环上，当满足发生条件的时候，就调用对应的处理方法
    task：任务，这是对协程对象的进一步封装，包含协程对象的各个状态
    future：代表将来执行或者没有执行的任务的结果，实际上和 task 没有本质区别
    """

# 随着 Python 的更新，上面的写法已经不再适用
def async_intro02():
    # 定义一个 execute() 方法
    async def execute(x):
        print('运行 execute 函数:', x)

    # 使用 asyncio.run() 来运行协程
    asyncio.run(execute(1))

    # 这行代码将在协程执行完毕后执行
    print('loop')

    # 运行 execute 函数: 1
    # loop

def async_intro03():
    # 定义一个 execute() 方法
    async def execute(x):
        print('运行 execute 函数:', x)
        return x

    # 直接调用后并不会执行，而是返回一个 coroutine 对象
    coroutine = execute(1)
    print('coroutine 对象:', coroutine)

    # 创建一个事件循环 loop
    loop = asyncio.get_event_loop()
    # 将协程对象转化为 task 对象
    task = loop.create_task(coroutine)
    print('转化 task:', task)
    # 将task对象注册到事件循环中
    loop.run_until_complete(task)
    print('注册 task:', task)
    print('loop')

    # coroutine 对象: <coroutine object async_intro03.<locals>.execute at 0x0000023685123510>
    # 转化 task: <Task pending name='Task-1' coro=<async_intro03.<locals>.execute() running at D:\workspace\py_web_crawler_dev_practice\chapter06\async_base.py:52>>
    # 运行 execute 函数: 1
    # 注册 task: <Task finished name='Task-1' coro=<async_intro03.<locals>.execute() done, defined at D:\workspace\py_web_crawler_dev_practice\chapter06\async_base.py:52> result=1>
    # loop

def async_intro04():
    # 定义一个 execute() 方法
    async def execute(x):
        print('运行 execute 函数:', x)
        return x

    # 直接调用后并不会执行，而是返回一个 coroutine 对象
    coroutine = execute(1)
    print('coroutine 对象:', coroutine)

    # 定义 task 对象
    task = asyncio.ensure_future(coroutine)
    # 创建一个事件循环 loop
    loop = asyncio.get_event_loop()
    # 将 task 对象注册到事件循环中
    loop.run_until_complete(task)
    print('注册 task:', task)
    print('loop')

    # coroutine 对象: <coroutine object async_intro04.<locals>.execute at 0x0000013DAF7D3510>
    # 运行 execute 函数: 1
    # 注册 task: <Task finished name='Task-1' coro=<async_intro04.<locals>.execute() done, defined at D:\workspace\py_web_crawler_dev_practice\chapter06\async_base.py:79> result=1>
    # loop

# async_intro01()
# async_intro02()
# async_intro03()
# async_intro04()
