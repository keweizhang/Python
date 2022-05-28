# 关键字 `None`

None表示空，但不等于任何其他数据类型的空，它不等于空字符串、空列表，也不等同于False
```python
a = ''
b = False
c = []

print(a==None)      # 返回False
print(b==None)      # 返回False
print(c==None)      # 返回False
print(a is None)    # 返回False
```

