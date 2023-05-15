# 数据解析方式之xpath

![img_1.png](..%2Fimg%2Fimg_1.png)

> * `xpath`属于`xml`/`html`解析数据的一种方式，基于元素（`Element`）的树形结构(`Node`>`Element`)
> * 选择某一元素时,根据元素的路径选择,如`/htm1/head/title`获取`<title>`标签

## 绝对路径

> * 从根标签开始，按`tree`结构依次向下查询。

## 相对路径

相对路径可以有以下写法

> * 相对于整个文档
>
>   * `//img`
>   * 查找出文档中所有的`<img>`标签元素
> * 相对于当前节点
>
>   * `//table`
>   * 假如当前节点是`<table>`,查找它的`<img>`的路径的写法
>
>     * `.//img`


## 数据提取

> * 提取文本
>
>   * `//title/text()`
> * 提取属性
>
>   * `//img/@href`
> * 提取指定位置的元素
>
>   * 获取网页中的数据类型与字符集,获取第一个`<meta>`标签
>
>     * `//meta[0]//@content`
>     * `//meta[first(]//@content`
>   * 获取最后一个`<meta>`标签
>
>     * `//meta[last()]//@content`
>   * 获取倒数第二个`<meta>`标签
>
>     * `//meta[position(-2]//@content`
>   * 获取前三个`<meta>`标签
>
>     * `//meta[position()<3]//@content`
> * 指定属性条件
>
>   * 查找`class`为`circle-img`的`<img>`标签
>
>     * `//img[@class="circle-img"]`