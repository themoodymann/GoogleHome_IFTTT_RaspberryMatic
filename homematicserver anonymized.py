# Written by Roger Wattenhofer, on a fun afternoon.

# Python Program that connects IFTTT with RaspberryMatic
# First fix all the TODOs in this piece of code.
# Then have this running on any machine that is accessible through the internet

from selenium import webdriver
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 9999 # TODO: This is the PORT number of your "server", as addressed by IFTTT. Choose any number you like.
# TODO: Attention, you must make sure that this port number is reachable enabling port forwarding on your modem/router.

# TODO: What follows are the commands supported by RaspberryMatic. The left item (e.g., closewindow) is what you call from IFTTT
# TODO: This program then clicks the command on the right (homescreen of web interface of RaspberryMatic, e.g. //table[@id='1264Locked'])
# TODO: This is an XPath, you can find this XPath when on the (homescreen of web interface of your RaspberryMatic)...
# TODO: ... by using a Browser extension like XPath Helper (Shift+Click on the clickable element, and then use the important bit towards the end of the string)

commands = {b'closewindow':"//table[@id='1264Locked']", 
            b'openwindow':"//table[@id='1264Open']",
            b'loudneighbors':"//div[@id='1545Start']",
            b'openandclose':"// div[@id='1609Start']",
            b'blindsdown':"//table[@id='1369Down']",
            b'blindsup':"//table[@id='1369Up']"}

def homeaticCommand(command):
    driver = webdriver.Chrome()
    driver.get("http://10.0.0.100") # TODO: This is the (local) IP address of your RaspberryMatic.
    if not command in commands.keys():
        print("command not found: ", command)
        return
    else:
        print("executing ",command)
    search_box = driver.find_elements_by_xpath(commands[command])
    search_box = search_box[0]
    search_box.click()
    driver.close()


# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

  # POST
  def do_POST(self):
        # print("do post")
        # Send response status code
        self.send_response(200)
        length = self.headers.get_all('Content-Length')
        length = int(length[0])
        # print(length)
        post_body = self.rfile.read(length)
        # print(post_body)
        homeaticCommand(post_body)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

  # GET
  def do_GET(self):
        return

def run():
  # print('starting server...')
  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('', PORT) # TODO: Fix this with the IP address of the machine this code is running.
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('server running...')
  httpd.serve_forever()

run()


