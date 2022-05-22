# Python语法

## 1. [变量与运算符](https://github.com/keweizhang/Notes/blob/main/Python/py_Variables.md)


## 2. 数据类型

|数据类型|简要说明|数据类型|简要说明|
|----|----|---|---|
|[字符串](https://github.com/keweizhang/Notes/blob/main/Python/DataType/py_DataType_Str.md)|熟悉常用方法|[格式化字符串](https://github.com/keweizhang/Notes/blob/main/Python/DataType/py_DataType_StrFormat.md)和[格式化符](https://github.com/keweizhang/Notes/blob/main/Python/DataType/py_DataType_StrFormator.md)|用于格式化输出|
|[列表](https://github.com/keweizhang/Notes/blob/main/Python/DataType/py_DataType_List.md)|内部元素可以不同类型|[集合](https://github.com/keweizhang/Notes/blob/main/Python/DataType/py_DataType_Set.md)|无序不重复|
|[元组](https://github.com/keweizhang/Notes/blob/main/Python/DataType/py_DataType_Tuple.md)|无序的列表|[字典](https://github.com/keweizhang/Notes/blob/main/Python/DataType/py_DataType_Dict.md)|无序键值对的集合|


## 3. [结构](https://github.com/keweizhang/Notes/blob/main/Python/py_Structure.md)
## 3. 结构

### 3.1 `if-else`分支结构

|关键字|用法|关键字|用法|
|---|---|---|---|
|`if condition:`|根据`condition`逻辑值判定是否要执行代码块|||
|`elif`|用于多个条件的判断|`else:`|用于全部剩余情况的判断|

:information_source: 判断的优雅方式为`if x:`，而不是 `if x == True:` 

:information_source: 判定条件可以为逻辑值或者表达式，当结果为`True`、`非0`、`非空`时判定为真

```python
if condition1:
    expression1
elif condition2:
    expression2
else:
    expression3
```

### 3.2 循环结构

|关键字|用法|关键字|用法|
|---|---|---|---|
|`while`|循环直到条件改变|`continue`|跳过剩余代码进入下一次循环|
|`for`|循环给定的可迭代对象|`break`|跳出当前整体循环|

:information_source: `continue` 和 `break` 通常配合`if`语句使用

#### `while`循环

适用于循环次数不确定，但条件确定的情况

```python
# 对 condition 进行判定，需要配合用来改变条件的 increacement语句
while condition:
    expression
    increacement
# 用 break 判定，以结束循环
while True:
    expression
    if condition:
        break
```

也可以直接 `while True:`，在循环体内提供判定条件，再`break` 结束循环

#### `for`循环结构

适用于循环次数或者内容确定的情况

```python
for elem in elements: 
    exprestion
```

`elem` 为临时变量，可以在`for`循环内调用，`elements` 可以为**任何可迭代的数据对象**

:information_source: 如果需要循环规律数列，可以配合`range()`函数使用

### 1.4 函数

### 1.5 类

### 1.6 文件

### 1.7 异常

### 1.8 关键字
|关键字|作用|关键字|作用|关键字|作用|
|----|----|----|----|----|----|
| `True` | 布尔类型 `真` | `False` | 布尔类型 `假` | `None` |特殊数据类型 `空`|
| `and` | 逻辑 `与` | `or` | 逻辑 `或` | `not` | 逻辑 `非` |

|关键字|作用|关键字|作用
|----|----|----|----|
| `in` | 判断元素存在和遍历 | `with` | 自动处理异常，常用在文件读写 |
| `as` | 名称代替或赋值 |||

#### 常用在异常处理中的关键字
|关键字|作用|关键字|作用
|----|----|----|----|
| `try` | 判断元素存在和遍历 | `raise`| 抛出异常（可自定义）
| `except` | 处理异常，规范发生异常时的程序反馈 | `assert` | 直接根据主动设置的判断条件返回错误提示，而不是等异常发生时|
| `else` | 当`try`代码块没有异常抛出时执行| `pass` |可以用在错误发生时直接忽略，不给任何反馈而跳过|
| `finally` | 是否发生异常都要执行 ||

## 2-常用操作

[遍历](https://github.com/keweizhang/Notes/blob/main/Python/Operation/pyTraversal.md)


