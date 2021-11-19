from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi
#cgi = common gateway interface....processes information submitted through a form

taskList = ['Task 1', 'Task 2', 'Task 3']
#what will be displayed by the HTML below

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        #if self.path.endswith will take in each webpage
        if self.path.endswith('/tasklist'):
            self.send_response(200)
            #this is required as the 200 is essential for get requests
            self.send_header('content-type', 'text/html')
            self.end_headers()

            output = ''
            output += '<html><body>'
            output += '<h1>Task List</h1>'
            output += '<h3><a href="/tasklist/new">Add New Task</a></h3>'
            for task in taskList:
                output += task
                output += '<a/ href="/tasklist/%s/remove">X</a>' % task
                output += '</br>'
            output += '</body><html>'
            self.wfile.write(output.encode())
            #encodes the html

        if self.path.endswith('/new'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()

            output = ''
            output += '<html><body>'
            output += '<h1>Add Task List</h1>'
                      #form starts below -------
            output += """<form method="POST" enctype="multipart/form-data"
                      action="/tasklist/new">"""
            output += '<input name="task" type="text" placeholder="Add new task">'
            output += '<input type="submit" value="Add">'
            output += '</form>'
                      #form finishes above -------
            output += '</body><html>'
            self.wfile.write(output.encode())

        if self.path.endswith('/remove'):
            listIDPath = self.path.split('/')[2]
            print(listIDPath)
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()

            output = ''
            output += '<html><body>'
            output += '<h1>Remove task: %s</h1>' % listIDPath.replace('%20', ' ')
            output += """<form method="POST" enctype="multipart/form-data"
                      action="/tasklist/%s/remove">""" % listIDPath
            output += '<input type="submit" value="Remove"></form>'
            output += '<a href="/tasklist">Cancel</a>'
            output += '</body><html>'
            self.wfile.write(output.encode())

    def do_POST(self):
        if self.path.endswith('/new'):
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))

            #cgi.parse_header prints the following:
            #('multipart/form-data',
            #{'boundary': '----WebKitFormBoundarySI9zI5IsHSljghMR'})

            #the double variable takes in the first index of the tuple....
            #....to the first variable and the second index of the tuple to....
            #....the second variable
            #ctype is equal to the 1st index of the tuple, the entype section....
            #....of the form: "multipart/form-data"
            #pdict is equal to the 2nd index of the tuple, the boundary key....
            #....produced by the cgi.parse... command
            #a Boundary Key allows the server to separate the values in a form,....
            #....such as separating form_method, enctype, action etc

            #ctype therefore = 'multipart/form-data'
            #pdict therefore = ....
            #....{'boundary': '----WebKitFormBoundarySI9zI5IsHSljghMR'}

            #All 3 lines below are configurations
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            content_len = int(self.headers.get('Content-length'))
            pdict['CONTENT-LENGTH'] = content_len

            if ctype == 'multipart/form-data':

#THEN DO THE LOGIC NECESSARY / CHANGE THE BACKEND

                fields = cgi.parse_multipart(self.rfile, pdict)
                #cgi.parse_multipart will breakdown the form, and the pdict....
                #....will read the values separately.
                #The only value that this will return will be 'task':
                #{'task': ['My Input']}
                new_task = fields.get('task')
                #this will simply get the task value - 'My Input'
                taskList.append(new_task[0])

#THEN REDIRECT TO THE FRONT END

            self.send_response(301) #301 is a redirect command, rather than a....
            #....200 which simply gets.
            #The location of the redirect is in the 2nd send_header line....
            #....below (/tasklist)
            self.send_header('content-type', 'text/html')
            self.send_header('Location', '/tasklist')
            self.end_headers()

        if self.path.endswith('/remove'):
            listIDPath = self.path.split('/')[2]
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))

            if ctype == 'multipart/form-data':
                list_item = listIDPath.replace('%20', ' ')
                taskList.remove(list_item)
            self.send_response(301)
            self.send_header('content-type', 'text/html')
            self.send_header('Location', '/tasklist')
            self.end_headers()



def main():
    PORT = 8000
    server_address = ('localhost', PORT)
    server = HTTPServer(server_address, requestHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()
