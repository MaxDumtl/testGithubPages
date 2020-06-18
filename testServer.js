var http = require("http");  
var server = http.createServer(function(request, response) {  
    response.writeHead(200, {  
        'Content-Type': 'text/plain'  
    });  
    response.write("This is Test Message.");  
    response.end();  
});  
server.listen(8082); 