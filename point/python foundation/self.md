定义时需要而调用时又不需要  
self代表类的实例，而非类  
self.class则指向类。  
调用t.prt()时，实际上Python解释成Test.prt(t)，也就是说把self替换成类的实例。  

[参考](http://python.jobbole.com/81921/)