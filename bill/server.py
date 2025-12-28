from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs


class MyRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path.startswith("/name"):

            # Parse URL
            parsed_url = urlparse(self.path)
            query = parse_qs(parsed_url.query)

            # Get name value
            name = query.get("name", ["User"])[0]

            # Send response
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            message = f"Good evening {name}"
            self.wfile.write(message.encode())

        else:
            self.send_response(404)
            self.end_headers()


# Run server
server = HTTPServer(("localhost", 8000), MyRequestHandler)
print("Server running at http://localhost:8000")
server.serve_forever()
