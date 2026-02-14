from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Read the request body
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        data = json.loads(body)

        # Process it (this is where your "server logic" lives)
        user_message = data.get('message', '')
        response = {
            'echo': f'You said: "{user_message}" — processed by Python on the server!',
            'length': len(user_message)
        }

        # Send the response
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

