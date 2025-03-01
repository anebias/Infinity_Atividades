const http = require('http');

const server = http.createServer((req,res) => {
    if (req.url === '/json'){
        res.writeHead(200,{'Content-Type': 'application/json'});
        res.end(JSON.stringify({message:'Hello, JSON!'}))
    } 
    else {
        res.writeHead(200,{'Content-Type':'text/html'});
        res.end('<h1>Hello, HTML!! </h1>')
    }})

    server.listen(3000,() => {
        console.log('Servidor rodando em http://localhost:3000')
    });