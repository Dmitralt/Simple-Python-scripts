from http.server import BaseHTTPRequestHandler, HTTPServer
from re import escape

from src.modules import send_json_answer,request_information,default_answer
from src.requests import CUSTOMERS_POST,CUSTOMERS_GET,CUSTOMERS_DELETE,CUSTOMERS_PUT
import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["my_python_database"]

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    
    def do_POST(self):        
        data=request_information(self)        
        answer = ""
        if (data["path"][1]=="customers"):
            answer = CUSTOMERS_POST(mydb,data)
            send_json_answer(self,answer)
        else:
            default_answer(self)

    def do_GET(self):        
        data=request_information(self)
        if (data["path"][1]=="customers"):        
            answer =  CUSTOMERS_GET(mydb,data)       
            send_json_answer(self,answer)
        else:
            default_answer(self)


    def do_DELETE(self):        
        data=request_information(self)
        if (data["path"][1]=="customers"):        
            answer =  CUSTOMERS_DELETE(mydb,data)       
            send_json_answer(self,answer)
        else:
            default_answer(self)

    def do_PUT(self):        
        data=request_information(self)
        if (data["path"][1]=="customers"):        
            answer =  CUSTOMERS_PUT(mydb,data)       
            send_json_answer(self,answer)  
        else:
            default_answer(self)           


if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        myclient.close()
        pass

    webServer.server_close()
    print("Server stopped.")