# -*- coding:utf-8 -*-

import BaseHTTPServer

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	'''处理请求并返回页面'''

	#页面模板
	Page = '''\
		<html>
		<body>
		<p>hello,web!</p>
		</body>
		</html>
	'''

	#处理get请求
	def do_GET(self):
		self.send_response(200)#send_response（）：发送应答消息和状态码
		self.send_header("content-Type","text/html")
		self.send_header("Content-Length",str(len(self.Page)))
		self.end_headers()
		#wfile：wfile 是一个输出流，用来回写响应，回写的数据必须遵守 HTTP 协议的格式
		self.wfile.write(self.Page)

# ---------------------------------------------------------
if __name__=='__main':#直接执行这个脚本时才会向下执行，脚本由其他脚本引入不执行
	serverAddress=('',8080)#服务器地址
	#client_address客户端的地址，存放在一个 tuple 里 (host, port)
	server = BaseHTTPServer.HTTPServer(serverAddress,RequestHandler)#创建server 实例
	server.serve_forever()#不停的执行server


#send_response（）：发送应答消息和状态码
#wfile：wfile 是一个输出流，用来回写响应，回写的数据必须遵守 HTTP 协议的格式
