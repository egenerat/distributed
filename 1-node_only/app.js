var http = require('http');

var server = http.createServer(function(req, res) {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'application/json');
  res.write(JSON.stringify({ hello: 'world' }));
  res.end();
});
server.listen(8080);
