from http.server import HTTPServer, BaseHTTPRequestHandler
from view import *
import cgi
from shop import *

submitted_search = []

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('/'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            view_file = ''
            view_file += InterfaceText().home_page()
            self.wfile.write(view_file.encode())

        if self.path.endswith('/search-results'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            search = ''
            search += InterfaceText().search_results()
            self.wfile.write(search.encode())

        if self.path.endswith('/view-basket'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            search = ''
            search += InterfaceText().view_basket()
            self.wfile.write(search.encode())

    def do_POST(self):
        if self.path.endswith('/search-results'):
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            content_len = int(self.headers.get('Content-length'))
            pdict['CONTENT-LENGTH'] = content_len
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                searched = fields.get('search')
                submitted_search.append(searched[0])
                print(submitted_search)

        self.send_response(301)
        self.send_header('content-type', 'text/html')
        self.send_header('Location', '/search-results')
        self.end_headers()


def main():
    PORT = 8000
    server_address = ('localhost', PORT)
    server = HTTPServer(server_address, requestHandler)
    print('Server running on Port %s' % PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()
