import sipfullproxy
import SocketServer
import socket
import sys
import logging



vals = input("Chces nastavit custom hodnoty pre port a ip host? Ak ano stlac 1 inak 2")
start_call = False
#sipfullproxy.start_call = False

if vals == 1:
    PORT = input("Zadaj port")
    HOST = raw_input("Zadaj ip adresu proxy")
else:
    HOST, PORT = '10.10.57.87', 5060

hostname = socket.gethostname()
logging.info(hostname)
ipaddress = socket.gethostbyname(hostname)
if ipaddress == "127.0.0.1":
    ipaddress = sys.argv[1]
sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, PORT)
sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, PORT)
server = SocketServer.UDPServer((HOST, PORT), sipfullproxy.UDPHandler)
server.serve_forever()
