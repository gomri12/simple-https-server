# written by Omri Glam 
# generate cert.pem for one year with the following command:
#    openssl req -new -x509 -keyout cert.pem -out cert.pem -days 365 -nodes
# save the cert.pem in the same folder of the script
# run the script:
#    python simple-https-server.py
# then in your browser, visit:
#    https://localhost:81
# Notice that if you want to run it on server and connect to it from outside you need to change 'localhost' --> '0.0.0.0'

from http.server import HTTPServer, SimpleHTTPRequestHandler
import logging
import ssl

class GetHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.error(self.headers)
        SimpleHTTPRequestHandler.do_GET(self)

Handler = GetHandler		
httpd = HTTPServer(('localhost', 81), Handler)
httpd.socket = ssl.wrap_socket(httpd.socket, certfile='./cert.pem', server_side=True)
httpd.serve_forever()