from http.server import SimpleHTTPRequestHandler
from http.server import CGIHTTPRequestHandler
from http.server import ThreadingHTTPServer
from functools import partial
import contextlib
import sys
import os
from threading import Thread

from render import RenderStatement
from pdf import PDF


class DualStackServer(ThreadingHTTPServer):
    def server_bind(self):
        # suppress exception when protocol is IPv4
        with contextlib.suppress(Exception):
            self.socket.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
        super().server_bind()

def start_server_thread(port, bind, cgi, directory):
    """启动服务器的线程，并返回服务器实例"""
    handler_class = CGIHTTPRequestHandler if cgi else SimpleHTTPRequestHandler
    httpd = ThreadingHTTPServer((bind, port), partial(handler_class, directory=directory))

    def run_server():
        print(f"Serving HTTP on {bind} port {port} (http://{bind}:{port}/) ...")
        httpd.serve_forever()

    server_thread = Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()
    return httpd

def stop_server(httpd):
    """停止服务器"""
    httpd.shutdown()

if __name__ == '__main__':
    statement = RenderStatement()
    html = statement.render_to_html()
    with open('output.html', 'w') as f:
        f.write(html)
    httpd = start_server_thread(port=5000, bind='127.0.0.1', cgi=False, directory=os.getcwd())
    try:
        pdf = PDF()
        pdf.generate_pdf('http://127.0.0.1:5000/output.html', 'result/output.pdf')
        print('PDF generated successfully')
    finally:
        stop_server(httpd)
