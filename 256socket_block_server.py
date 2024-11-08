from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import time

# 단일 응답을 제공할 포트 번호 설정
RESPONDING_PORT = 8000

class CustomHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.server.server_port == RESPONDING_PORT:
            # 8000번 포트에서만 응답을 제공
            if self.path == "/delayed":
                time.sleep(15)  # 지연 응답
                self.send_response(200)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                self.wfile.write(b"Delayed response after 15 seconds")
            else:
                self.send_response(404)
                self.end_headers()
        else:
            # 다른 모든 포트는 블락 상태 유지
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.send_header('Connection', 'close')
            self.end_headers()
            while True:
                time.sleep(1)  # 무한 대기

def run_server(port):
    server_address = ('', port)
    httpd = HTTPServer(server_address, CustomHandler)
    print(f"서버가 {port}번 포트에서 실행 중...")
    httpd.serve_forever()

if __name__ == "__main__":
    # 8000~8255 포트에서 서버 실행
    ports = range(8000, 8256)
    for port in ports:
        threading.Thread(target=run_server, args=(port,), daemon=True).start()

    # 메인 스레드를 유지하여 서버가 종료되지 않도록 함
    while True:
        time.sleep(1)
