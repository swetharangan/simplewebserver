from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
         <title>simplewebserver</title>
    </head>
    <body>
        <table align="center" border="2" cellspacing="12" cellpadding="12" height="25" width="50">
        <h1 align="center" >top 5 software companies with revenue</h1>
            <tr>
            
                <th>RANK</th>
                <th>COMPANY</th>
                <th>REVENUE</th>
            </tr>
            <tr>
                <td>1</td>
                <td>Microsoft</td>
                <td>$86.8</td>
            </tr>
            <tr>
                <td>2</td>
                <td>oracle</td>
                <td>$37.1</td>
            </tr>
            <tr>
                <td>3</td>
                <td>SAP</td>
                <td>$20.9</td>
            </tr>
             <tr>
                <td>4</td>
                <td>symantec</td>
                <td>$6.8</td>
            </tr>
             <tr>
                <td>5</td>
                <td>VMware</td>
                <td>$5.2</td>
            </tr>
        </table>
    </body>
<html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()