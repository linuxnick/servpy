# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import webbrowser

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        from rss_parser import Parser
        from requests import get
        rss_url = "https://www.psxhax.com/articles/index.rss"
        xml = get(rss_url)
        parser = Parser(xml=xml.content, limit=None)
        feed = parser.parse()
        ita = 1
        feed2 = " "
        for item in feed.feed:
            feed2 = feed2 + "<br>" + item.title
        self.wfile.write(bytes("<p> %s </p>" % feed2, "utf-8" ))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    webbrowser.open('http://localhost:8080')

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")


