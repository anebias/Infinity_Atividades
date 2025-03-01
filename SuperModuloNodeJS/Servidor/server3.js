const http = require('http');

const server = http.createServer((req,res) => {
    if (req.url === '/'){
        res.writeHead(200,{'Content-Type': 'text/plain'});
        res.end(JSON.stringify({message:'Home Page!'}))
    } 
    else if (req.url === '/sobre'){
        res.writeHead(200,{'Content-Type':'text/plain'});
        res.end('Página Sobre')
    }
    else{
        res.writeHead('Content-Type': 'text/plain');
        res.end('Página não encontrada')
    }})

    server.listen(3000,() => {
        console.log('Servidor rodando em http://localhost:3000')
    });