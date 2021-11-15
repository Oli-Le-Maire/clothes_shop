from http.server import HTTPServer, BaseHTTPRequestHandler
from view import *

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('/'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            words = ''
            words += '<html><body>'
            words += InterfaceText().test()
            words += '</html></body>'
            self.wfile.write(words.encode())

def main():
    PORT = 8000
    server_address = ('localhost', PORT)
    server = HTTPServer(server_address, requestHandler)
    print('Server running on Port %s' % PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()
