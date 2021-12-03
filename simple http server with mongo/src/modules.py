import json
from furl import furl

def send_json_answer(self,data):
    self.send_response(200)
    self.send_header("Content-type", "application/json")
    self.end_headers()      
    self.wfile.write(bytes(json.dumps(data), "utf-8"))

def request_information(self):
    Answer={"path":"","url_params":{},"request_json":{}}
    self.data_string = self.rfile.read(int(self.headers['Content-Length'])) 
    f = furl(self.path) 
    Answer["path"]=self.path.split('?')[0].split('/')
    Answer["url_params"]=f.args
    try:
        Answer["request_json"]=json.loads(self.data_string)
    except ValueError as e:
        Answer["request_json"]={}
    return Answer


def default_answer(self):
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()

    self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
    self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
    self.wfile.write(bytes("<body>", "utf-8"))
    self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
    self.wfile.write(bytes("</body></html>", "utf-8"))