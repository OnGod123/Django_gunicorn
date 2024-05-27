import http.server
import socketserver
import os

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Specify the path to your file
        file_path = "alx-system_engineering-devops/0x15-api/1-export_to_CSV.py"

        if not os.path.isfile(file_path):
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'File not found')
            print(f"File not found: {file_path}")
            return

        try:
            # Open and read the file
            with open(file_path, "rb") as file:
                file_content = file.read()

            # Extract the filename from the file path
            file_name = os.path.basename(file_path)
            print(f"Serving file: {file_name}")

            # Send the response headers
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.send_header('Content-Disposition', f'attachment; filename="{file_name}"')
            self.end_headers()

            # Send the file content as response
            self.wfile.write(file_content)

        except Exception as e:
            # Catch any other exceptions and log the error
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b'Internal server error')
            print(f"Error serving file: {e}")

PORT = 8000

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Server started on port {PORT}")
    httpd.serve_forever()

