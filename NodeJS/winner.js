var http = require('http');
var mysql = require('mysql');

var con = mysql.createConnection({
	host: 'localhost',
	user: 'root', 
	password: 'Password1',
	database: 'winner',
	charset: "utf8_general_ci"
});

con.connect(function(err){
	if(err)
	{
		console.log('Error Connectin to DB!');
	}
	console.log('Connection Established!');
});

con.query('set names utf8', function(err, result) {
  // Neat!
});

http.createServer(function(request, response){

	var returned_data = "<html dir='rtl'><meta charset='UTF-8' /><center><table>";

	con.query('select * from bets order by bet_id', function(err, rows){
		if(err)
		{
			throw err;
		}

		for(var i = 0; i < rows.length; i++)
		{
			var color = "";
			var ratio = rows[i]['ratio'];
			if(ratio < 1.5)
			{
				color = "rgba(255, 0, 0, 0.4)"; //Red
			}
			else
			{
				if(ratio < 2)
				{
					color = "rgba(255, 255, 102, 0.4)"; //Yellow
				}
				else
				{
					if(ratio < 3)
					{
						color = "rgba(153, 255, 102, 0.4)"; //Green
					}
					else
					{
						color = "rgba(0, 255, 0, 0.4)"; //Greener
					}
				}
			}
			var add_data = "<tr>" + 
						"<td>" + rows[i]['team'] + 
						"</td><td>" + rows[i]['bet_id'] + 
						"</td><td style='background-color:" + color + "'>" + rows[i]['ratio'] + 
						"</td></tr>";
			returned_data += add_data;
		}

		returned_data += "</table></center></html>";

		response.writeHead(200, {'Content-Type': 'text/html'});
		response.end(returned_data);
	});


}).listen(8080);