const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require('ip');



http.createServer((req, res) => {
  if (req.url === "/") {
      fs.readFile("./public/index.html", "UTF-8", (err, body) => {
      res.writeHead(200, {"Content-Type": "text/html"});
      res.end(body);
    });
  } else if(req.url.match("/sysinfo")) {
    myHostName=os.hostname();
    TotalMem = os.totalmem();
    FreeMem = os.freemem();
    numCpus = os.cpus().length;

    // Server Uptime
    var utSec = os.uptime();
    var utMin = utSec/60;
    var utHour = utMin/60;
    var utDay = utHour/24;

    utSec = Math.floor(utSec);
    utMin = Math.floor(utMin);
    utHour = Math.floor(utHour);
    utDay = Math.floor(utDay);
    

    utDay = utDay%24;
    utHour = utHour%60;
    utMin = utMin%60;
    utSec = utSec%60;

    html=`
    <!DOCTYPE html>
    <html>
      <head>
        <title>Node JS Response</title>
      </head>
      <body>
        <p>Hostname: ${myHostName}</p>
        <p>IP: ${ip.address()}</p>
        <p>Server Uptime:Days: ${utDay}, Hours: ${utHour}, Minutes: ${utMin}, Seconds: ${utSec}</p>
        <p>Total Memory:${(TotalMem / (1024 * 1024))} MB</p>
        <p>Free Memory:${(FreeMem / (1024 * 1024))} MB</p>
        <p>Number of CPUs: ${numCpus}</p>
      </body>
    </html>`
    res.writeHead(200, {"Content-Type": "text/html"});
    res.end(html);
  } else {
    res.writeHead(404, {"Content-Type": "text/plain"});
    res.end(`404 File Not Found at ${req.url}`);
  }
}).listen(3000);

console.log("Server listening on port 3000");
