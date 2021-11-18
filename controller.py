from http.server import HTTPServer, BaseHTTPRequestHandler
from view import *
import cgi
from model import *

submitted_search = []

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('/'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            home_page = ''
            home_page += View().home_page()
            self.wfile.write(home_page.encode())

        if self.path.endswith('/search-results'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            response = Model().check_the_stock(submitted_search[0])
            search_results_page = ''
            search_results_page += View().search_results(response)
            self.wfile.write(search_results_page.encode())

        if self.path.endswith('/view-basket'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            view_basket_page = ''
            view_basket_page += View().view_basket()
            self.wfile.write(view_basket_page.encode())

    def do_POST(self):
        if self.path.endswith('/search-results'):
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            content_len = int(self.headers.get('Content-length'))
            pdict['CONTENT-LENGTH'] = content_len
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                user_search = fields.get('search')
                submitted_search.append(user_search[0])

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
