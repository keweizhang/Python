# 通用操作

`len()`函数用于获取序列类型数据的长度

`type()`函数用来获取变量的数据类型

## 判断元素存在

`elem in elements` 会返回布尔值`Ture`, `False` 

适用：str list tuple set dict 

## 遍历

### 列表，字符串

`str`, `list`，使用`for elem in elems:` 会按顺序遍历元素

### 元组，集合

`tuple`,`set` ，使用 `for elem in elems:` 会无序地遍历元素

### 字典

`for elem in elems:` 会无序地遍历字典key 

`for elem in elems.items():` 会无序地遍历字典，得到`(key,value)` 格式的`tuple`数据

`for elem1,elem2 in elems.items():` 会无序地遍历字典，前后两个变量分别为`key`和`value`

### `enumerate()` 函数

遍历时得到元素索引，适用于所有序列类型，只返回两个值，索引和数据

#### `str`, `list`, `tuple`, `set`

使用`for index,elem in enumerate(elements):` 即可得到索引和元素

#### `dict`

使用`for index,elem in enumerate(elements):` 会返回索引和`(key,value)`组成的tuple ，不可直接三个变量接收

使用`for index,(elem1,elem2) in enumerate(elements):` 可以直接得到 索引、键、值

zip() 函数

### 同时遍历两个序列

使用`zip()`函数

`for i,j in zip(A,B):` 相当于遍历A B组成的二维列表`(a1,b1)..(an,bn)`，长度不同时，按短的结束遍历

注意：并不是遍历组合，与嵌套循环不同

```python
A = list(range(1,10))
B = list(range(2,11))

for i,j in zip(A,B):
    print(f'i is {i}, j is {j}')
    
i is 1, j is 2
i is 2, j is 3
i is 3, j is 4
i is 4, j is 5
i is 5, j is 6
i is 6, j is 7
i is 7, j is 8
i is 8, j is 9
i is 9, j is 10
```

