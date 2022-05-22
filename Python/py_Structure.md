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
