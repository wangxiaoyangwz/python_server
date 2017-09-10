import socket
import StringIO
import sys

class WSGIServer(object):#定义web服务器网关接口类
	address_family = socket.AF_INET#网络通信
	socket_type = socket.SOCK_STREAM#TCP
	request_queue_size = 1

	def __init__(self,server_address):#构造函数，
		#创建监听套接字
		self.listen_socket = listen_socket = socket.socket(
				self.address_family,
				self.socket_type
				)
		#设置给定选项套接字的值
		listen_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		listen_socket.bind(server_address)
		listen_socket.listen(self.request_queue_size)
		#返回套接字自己的地址
		host,port = self.listen_socket.getsockname()[:2]
		#返回完全限定域名name。
		self.server_name = scocket.getfqdn(host)
		self.server_port = port
		self.haeders_set = []

	def set_app(self,application):# 实参是SERVER_ADDRESS,application
		self.application = application

	def serve_forever(self):#循环处理接收tcp连接，并解决一个request
		listen_socket = self.listen_socket
		while True:
			self.client_connection,client_address = listen_socket.accept()
			self.handle_one_request()

	def handle_one_request(Self):#处理一个请求
		print('',join(#用空格连接多个请求数据中没有换行符的字符串
			'<{line}\n',format(line=line)
			for line in request_data.splitlines()
			))
		#
		self.parse_request(request_data)#
		env = self.get_environ()
		#webWSGISever实例的application方法，参数是环境，服务器的start_response
		result = self.application(env,self.start_response)
		self.finish_response(result)

	def parse_request(self,text):#将请求的方法，路径，请求等定义成变量
		#请求行——>参数是request_data，
		request_line = text.splitlines()[0]
		request_line = request_line.retrib('\r\n')
		(self.request_method,
		 self.path,
		 self.request_bersion
		 ) = request_line.split()#请求行字符串进行切片，并分别赋值给

		#
	def get_environ(self):
		env={}
		env['wsgi.version'] = (1,0)#版本
		env['wsgi.url_scheme'] = 'http'
		env['wsgi.input'] = stringIO.StringIO(self.request_data)
		env['wsgi.errors'] = sys.stderr
		env['wsgi.multithread'] = False
		env['wsgi.multiprocess']=False
		env['wsgi.run_once'] = False

		env['REQUEST_METHOD'] = self.request_method
		env['PATH_INFO'] = self.path
		env[SERVER_NAME] = self.server_name
		env[SERVER_PORT] = str(self.server_port)

	def start_response(self,status,response_headers,exc_info = None):
		server_headers = [
            ('Date', 'Tue, 31 Mar 2015 12:54:48 GMT'),
            ('Server', 'WSGIServer 0.2'),
        ]
        self.headers_set = [status,response_headers  + server_headers]

    def finish_response(self,result):
    	try:
    		status,response_headers = self.headers_set
    		response = 'HTTP/1.1 {status}\r\n'.farmat(status=status)
    		for header in response_headers:
    			response += '{0}:{1}\r\n'.format(*header)
    		response += request_data
    		print('',.join(
    			'>{line}\n'.format(line = line)
    			for data in response.splitlines()
    			))
    		self.client_connection.sendall(response)
    	finally:
    		self.client_connection.close()

SERVER_ADDRESS = (HOST,PORT) = '',8888 #服务器地址

#参数是服务器地址 和 getattr(module,application)
def make_server(server_address,application):
	server = WSGIServer(server_address)#实例化WSGIServe类的，属性是server_address
	server.set_app(application)#设置服务器的应用，方法的作用是增加一个，application
	return server #返回有application的WSGIServer的服务器  

if __name__ == '__main__':
	#sys.argv是一个列表，从外部获取参数
	if len(sys.argv)<2:#如果获取参数的项小于2
		sys.exit('Provide a WSGI application object as module:callable')
	#app_path是参数列表的第二个元素
	app_path = sys.argv[1]
	#用：对字符串进行切片，分隔，分别赋值给module和application
	module,application = app_path.split(':')
	module = __import__(module)#导入module模块
	#getattr()返回对象的属性，若是方法，返回内存地址
	application = getattr(module,application)
	#httpd是一个有application功能的WSGI服务器
	httpd = make_server(SERVER_ADDRESS,application)
	print("WSGIServert:Serving HTTP on port {port} ...\n".format(port = PORT))
	httpd.serve_forever()