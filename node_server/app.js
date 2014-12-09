var express = require('express');
var bodyParser = require('body-parser')
var methodOverride = require('method-override');
var https = require('https')
var server_options = {
  key : fs.readFileSync('/etc/nginx/ssl/nginx.key').toString(),
  cert : fs.readFileSync('/etc/nginx/ssl/nginx.crt').toString()
}

var app = express();
var server = https.createServer(server_options, app).listen(8001)
var io = require('socket.io').listen(app);


io.set('browser client minification',true);
io.set('browser client gzip',true);

// Enables CORS
var enableCORS = function(req, res, next) {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS');
    res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization, Content-Length, X-Requested-With, *');

        // intercept OPTIONS method
    if ('OPTIONS' == req.method) {
        res.send(200);
    } else {
        next();
    };
};
app.use(enableCORS);
app.use(bodyParser());
app.use(methodOverride());


io.set('origins', '*:*');
console.log('Listening on port 8001');

app.post('/scrolls/ready', function (req, res) {
   io.emit('new-scroll', {user_id: req.body.user_id,
                        scroll_name: req.body.scroll_name});
   res.status(202);
   res.end();
});

app.get('/', function (req, res) {
    res.status(202);
   res.end();
});




io.on('connection', function (socket) {
  
});

