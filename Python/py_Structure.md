## 结构

### `if-else`分支结构

语法为：

```python
if condition1:
    expression1
elif condition2:
    expression2
else:
    expression3
```

`condition`可以为逻辑值，或者表达式，当其值或者表达式运算结果为`true`或者`非0`时，执行`:`后缩进的代码块

`elif`用于多个条件的判断

`else:`用于全部剩余情况的判断

:information_source: 判断的优雅方式为`if x:`，而不是 `if x == Ture:` 

### `while`循环结构

语法为：

```python
while condition:
    expression
    increacement
```

对`condition`进行判定，为真时，执行缩进内容

:information_source: 必须有改变判断条件的代码行，否则进入死循环，一般为类似`i += 1`

适用于循环次数不确定，但条件确定的情况

### `for`循环结构

语法为:

```python
for elem in elements: 
    exprestion
```

elem 为临时变量，可以在for循环内调用，elements 可以为任何可迭代的数据对象

:information_source: 如果需要循环规律数列，可以配合`range()`函数使用

### `break`语句

 跳出循环，通常配合`if`语句使用，当条件满足时，跳出当前整体循环

`continue`语句

跳过部分代码块，通常配合`if`语句使用，当条件满足时，跳过之后的代码块，进入下一次循环