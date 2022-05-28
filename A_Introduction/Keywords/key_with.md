# `with` 关键字

Python 中的 `with` 语句用于异常处理，封装了 `try…except…finally` 编码范式，提高了易用性。

with 语句使代码更清晰、更具可读性， 它简化了文件流等公共资源的管理。

## 直接打开文件
不使用 with，也不使用 try…except…finally
```python
file = open('./test_runoob.txt', 'w')
file.write('hello world !')
file.close()
```
以上代码在调用 `write` 的过程中，如果出现了异常，则 `close` 方法将无法被执行，因此资源就会一直被该程序占用而无法被释放

## 考虑异常
使用 `try…except…finally` 来改进代码：
```python
file = open('./test_runoob.txt', 'w')
try:
    file.write('hello world')
finally:
    file.close()
```
以上代码我们对可能发生异常的代码处进行 `try` 捕获，发生异常时执行 `except` 代码块，`finally` 代码块是无论什么情况都会执行，所以文件会被关闭，不会因为执行异常而占用资源。

## 使用 with 关键字

```python
with open('./test_runoob.txt', 'w') as file:
    file.write('hello world !')
```
使用 with 关键字系统会自动调用 f.close() 方法， with 的作用等效于 try/finally 语句是一样的。

with 语句实现原理建立在上下文管理器之上。

上下文管理器是一个实现 `__enter__` 和 `__exit__` 方法的类。

使用 with 语句确保在嵌套块的末尾调用 `__exit__` 方法。

这个概念类似于 `try...finally` 块的使用。
