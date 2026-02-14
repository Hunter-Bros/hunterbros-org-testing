from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Read the incoming request body
        content_length = int(self.headers.get("Content-Length", 0))
        raw_body = self.rfile.read(content_length)
        body = json.loads(raw_body)

        # Extract the message the user typed
        message = body.get("message", "")

        # Build the response
        response = json.dumps({
            "echo": f'You said: "{message}"',
            "length": len(message),
        })

        # Send it back
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(response.encode())