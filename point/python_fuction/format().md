# python之字符串格式化(format)

>它通过{}和:来代替传统%方式  

1)使用位置参数
```python
>>> li = ['hoho',18]
>>> 'my name is {} ,age {}'.format('hoho',18)
'my name is hoho ,age 18'
>>> 'my name is {1} ,age {0}'.format(10,'hoho')
'my name is hoho ,age 10'
>>> 'my name is {1} ,age {0} {1}'.format(10,'hoho')
'my name is hoho ,age 10 hoho'
>>> 'my name is {} ,age {}'.format(*li)
'my name is hoho ,age 18'
```  
2）使用关键字参数
```python
>>> hash = {'name':'hoho','age':18}
>>> 'my name is {name},age is {age}'.format(name='hoho',age=19)
'my name is hoho,age is 19'
>>> 'my name is {name},age is {age}'.format(**hash)
'my name is hoho,age is 18'
```  

3) 使用填充与格式化
```python
>>> '{0:*>10}'.format(10)  ##右对齐
'********10'
>>> '{0:*<10}'.format(10)  ##左对齐
'10********'
>>> '{0:*^10}'.format(10)  ##居中对齐
'****10****'
```  

4、精度与进制

```python
>>> '{0:.2f}'.format(1/3)
'0.33'
>>> '{0:b}'.format(10)    #二进制
'1010'
>>> '{0:o}'.format(10)     #八进制
'12'
>>> '{0:x}'.format(10)     #16进制
'a'
>>> '{:,}'.format(12369132698)  #千分位格式化
'12,369,132,698'
```
 

5、使用索引
```python
>>> li
['hoho', 18]
>>> 'name is {0[0]} age is {0[1]}'.format(li)
'name is hoho age is 18
```  

[参考](http://www.cnblogs.com/benric/p/4965224.html)