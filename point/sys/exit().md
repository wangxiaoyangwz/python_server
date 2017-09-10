##  Python os._exit() sys.exit() exit()区别  
Python`退出程序`的方式有两种：os._exit()， sys.exit()  
1. os._exit() 直接退出 Python程序，其后的代码也不会继续执行
2. sys.exit() 引发一个 SystemExit异常，若没有捕获这个异常，Python解释器会直接退出；捕获这个异常可以做一些额外的清理工作。0为正常退出，其他数值（1-127）为不正常，可抛异常事件供捕获。  
3. os._exit() 用于在线程中退出、sys.exit() 用于在主线程中退出。