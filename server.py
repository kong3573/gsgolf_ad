#!/usr/bin/env python3
"""
Naver Band Poster Web Viewer & Customizer Server
"""
import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run():
    server_address = ("", PORT)
    httpd = HTTPServer(server_address, Handler)
    print("==================================================")
    print(f"⛳ 광산골프 네이버 밴드 포스터 뷰어 서버 시작!")
    print(f"👉 웹 접속 주소: http://localhost:{PORT}")
    print("==================================================")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 서버가 종료되었습니다.")
        httpd.server_close()

if __name__ == "__main__":
    run()
