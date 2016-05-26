var http = require("http");
var mysql = require("mysql");
var requestIp = require('request-ip');

var con = mysql.createConnection({
	host : "localhost",
	user : "root",
	password : "Password1",
	database : 'general'
});

con.connect(function(err){
	if(err){
		//console.log('Error connecting to DB');
		return;
	}
	//console.log('Connection established');
});


http.createServer(function(request , response){
	response.writeHead(200 , {'Content-Type' : 'text/html'});

	var browser = request.headers['user-agent']

	var clientIp = requestIp.getClientIp(request); 

	clientIp = clientIp.substring(7);

	console.log(clientIp);

	//Log into DB the entery
	con.query("INSERT INTO enteries SET `ip` = '" + clientIp + "' ,  `browser` = '" + browser + "', `time` = CURRENT_TIMESTAMP" , function(err , res){
		if(err) throw err;
		//console.log('Last insert ID:' , res.insertID);
	});

	response.end(request.headers['user-agent']);
}).listen(8080);