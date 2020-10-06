import time
import grpc
import simple_pb2
import simple_pb2_grpc
import base64
from concurrent import futures

# シンプルサービスサーバーの定義
class SimpleServiceServicer(simple_pb2_grpc.SimpleServiceServicer):
    def __init__(self):
        pass
    
    def SimpleSend(self, request, context):
        text = 'This is TEST!'
        b64 = base64.encodestring(open('image.jpg', 'rb').read()).decode('utf8')
        return simple_pb2.SimpleResponse(text=text, image=b64)

# サーバーの開始
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
simple_pb2_grpc.add_SimpleServiceServicer_to_server(SimpleServiceServicer(), server)
server.add_insecure_port('[::]:50051')
server.start()
print('サーバーの開始')

# 待機
try:
   while True:
      time.sleep(3600)
except KeyboardInterrupt:
   # サーバーの停止
   server.stop(0)