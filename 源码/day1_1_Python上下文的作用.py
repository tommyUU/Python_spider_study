class A:
    def __enter__(self):
    # 进入上下文时，被调用的
    # 必须返回一个相关的对象
        print('--enter--')
        return 'Tommy'

    def __exit__(self, except_type, val, tb):
    # 退出上下文时，被调用的
    # except_type如果存在异常时，表示为异常类的实例对象
    # val异常的消息Message
    # tb 异常的跟踪栈
        print('--exit--')
    # 返回True表示存在异常不向外抛出
    # 返回False表示存在异常时，向外抛出
        return True

a = A()
with a as ret:
    print(ret)
    assert isinstance(ret, str)
    print('ok')