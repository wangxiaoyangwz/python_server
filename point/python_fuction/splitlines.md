# Python splitlines()方法  
`语法`：str.splitlines([keepends])
`参数`：keepends -- 在输出结果里是否去掉换行符('\r', '\r\n', \n')，默认为 False，不包含换行符，如果为 True，则保留换行符。
`返回值`：返回一个包含各行作为元素的列表
`实例 `：
```python
str1 = 'ab c\n\nde fg\rkl\r\n'
print str1.splitlines();

str2 = 'ab c\n\nde fg\rkl\r\n'
print str2.splitlines(True)

结果：
['ab c', '', 'de fg', 'kl']
['ab c\n', '\n', 'de fg\r', 'kl\r\n']
```