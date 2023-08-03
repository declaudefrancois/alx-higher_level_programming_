const http = require('http');
const fs = require('fs');
const path = require('path');
const hostname = '0.0.0.0';
const port = 3000;

const server = http.createServer((req, res) => {
  const url = req.url;
  if (url.endsWith('.ico')) {
    res.statusCode = 404;
    res.end('Not found');
    return;
  }
  const readStream = fs.createReadStream(path.join(__dirname, url));
  const mime = url.endsWith('.js') ? 'text/javascript' : 'text/html';
  res.writeHead(200, { 'Content-Type': mime });
  res.statusCode = 200;
  readStream.pipe(res);
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
