

const http = require("http");

const server = http.createServer((req, res) => {
  res.writeHead(200, {"Content-Type": "text/html"});

  res.end(`
    <!DOCTYPE html>
    <html>
      <head>
        <title>Node JS Response</title>
      </head>
      <body>
        <h1>Hello!</h1>
        <p>${req.url}</p>
        <p>${req.method}</p>
      </body>
    </html>
  `)
})

server.listen(3000)

console.log("Server listening on port 3000")