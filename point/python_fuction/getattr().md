# getattr(object,name[,default])  
功能：`获取`对象object的`属性或者方法`，如果存在`打印`下来，不存在，打印`默认值`，默认值可选  

注意：若`返回的是方法`，返回的时方法的`内存地址`，若想`运行这个方法`，在后面`加上一对括号`  

```python
>>> class test():
...     name="xiaohua"
...     def run(self):
...             return "HelloWord"
...
>>> t=test()
>>> getattr(t, "name") #获取name属性，存在就打印出来。
'xiaohua'
>>> getattr(t, "run")  #获取run方法，存在就打印出方法的内存地址。
<bound method test.run of <__main__.test instance at 0x0269C878>>
>>> getattr(t, "run")()  #获取run方法，后面加括号可以将这个方法运行。
'HelloWord'
>>> getattr(t, "age")  #获取一个不存在的属性。
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: test instance has no attribute 'age'
>>> getattr(t, "age","18")  #若属性不存在，返回一个默认值。
'18'
>>>
```  

