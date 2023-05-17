# 01、Python上下文

## 1.1什么是上下文

> * 任意的Python对象都可以使用上下文环境，使用`with`关键字。
> * 上下文是代码片段的区域
> * 当对象进入上下文环境时，解释器会调用对象的`__enter__()`
> * 当对象退出上下文环境时，会调用对象的`__exit__()`

## 1.2为什么使用

> * 对象在使用上下文环境时，为了确保对象正确的`释放资源`，避免出现`内存遗漏`。
> * 存在以下对象经常使用上下文`with`
>
>   * 文件操作对象`open()`
>   * 数据库的连接`db`
>   * 线程锁`Lock`

## 1.3如何使用

### 1.3.1重写类的方法

> * 上下文的两个核心方法
>
>   * ```python
>     class A:
>         def __enter__(self):
>         # 进入上下文时，被调用的
>         # 必须返回一个相关的对象
>             print('--enter--')
>             return 'disen'
>
>         def __exit__(self, except_type, val, tb):
>         # 退出上下文时，被调用的
>         # except_type如果存在异常时，表示为异常类的实例对象
>         # val异常的消息Message
>         # tb 异常的跟踪栈
>             print('--exit--')
>         # 返回True表示存在异常不向外抛出
>         # 返回False表示存在异常时，向外抛出
>             return True
>     ```

### 1.3.2 with中使用

```python
a =A()
with a as ret:
    print(ret)
    assert isinstance(ret,str)
    print('ok')
```