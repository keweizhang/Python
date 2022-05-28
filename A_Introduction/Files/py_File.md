# 1.6 文件读写

## 1.6.1 打开
函数 `open()` 接受文件名参数来打开指定文件

函数 `close()` 用来关闭文件

关键字 `with` 在不再需要访问文件后会自动将其关闭，避免因为错误导致`close()`未执行而带来的文件未关闭错误

因此简洁高效的方法就是用`with`配合`open`打开文件
```python
with open(file_name) as file_object:
    pass
```

## 1.6.2 读取
### 全部读取
使用方法`.read()`操作打开的文件对象，并将其结果作为一个长长的字符串存储在变量中

:information_source: `.read()`到达文件末尾时会返回一个空字符串，`print()`等操作时会多出一个空行，可以使用`.rstrip()`方法剔除

```python
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
```

### 逐行读取

使用`for`循环，遍历文件对象的每一行

:information_source: 每行末尾都有一个换行符，可以使用`.rstrip()`方法剔除

```python
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
```

### 读取为各行组成的列表

使用`.readlines()`方法，直接将文件对象转为该文件的每一行内容组成的列表

使用关键字`with`时，`open()`返回的文件对象只在`with`代码块内可用，但保存为列表后，可以供后续数据处理使用

```python
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
```

:warning: 不论哪种读取方式，得到的都是字符串，如果是需要处理的数值，必须进行类型转换

## 1.6.3 写入

### 写入方法
 `.write()` 将字符串写入文本，需要在打开文本时指定为写入或者追加模式

`open()`函数的参数：
|参数|含义|参数|含义|
|---|---|---|---|
|`'r'`|只读模式|`'w'`|写入模式|
|`'r+'`|读取和写入|`'a'`|追加模式|

如果写入的文件不存在，函数`open()`将自动创建。

:warning: 如果以写入（`'w'`）模式打开了已经存在的文件，内容会覆写，最好有判断文件是否存在的语句。常用为`os.path.isfile(filename)`

```python
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
```
### 写入多行
写入方法一样，需要注意在每行末尾设置好换行符
```python
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
```







