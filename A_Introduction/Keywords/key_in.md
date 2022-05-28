# 关键字 `in`

## 用于判断元素是否存在

`elem in elements` 会返回布尔值`Ture`, `False` 

适用： `str` `list` `tuple` `set` `dict` 等

用法举例：
```python
# 字符串
string = 'The Zen of Python, by Tim Peters'
print('of' in string)           # 返回 True
print('TimPeters' in string)    # 返回 False;Tim Peters中间有空格

# 列表
list1 = ['The','Zen','of','Python',',','by','Tim','Peters']
print('of' in list1)                    # 返回 True
print('Tim Peters' in list1)            # 返回 False
print('Tim Peters' not in list1)        # 返回 True
print('Tim' in list1,'Peters' in list1) # 返回 True True;

# 字典
dict1 = {'id':0,'winner':'jsr','age':'19940121','take_on':'vocal'}
print('id' in dict1)    # 返回 True；字典的键在字典里面
print(0 in dict1)       # 返回 False；字典的键对应的值不在字典里面
```

## 遍历
一般用于 `for` 循环内，对变量元素进行遍历
```python
# 列表，字符串
for elem in elems:  # 按顺序遍历元素

# 元组，集合
for elem in elems:  # 无序地遍历元素

# 字典
for elem in elems:  # 无序地遍历字典键key 
for elem in elems.items():  # 无序地遍历字典，得到(key,value)格式的tuple数据
for elem1,elem2 in elems.items():   # 无序地遍历字典，前后两个变量分别为key和value
```
