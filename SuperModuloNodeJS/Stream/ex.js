const express = require('express')
const app = express()
const PORT = 3000

app.use(express.json())

let usuarios= [
    {id: 1, nome: 'Maria'},
    {id:2, nome: 'João'}
    ] 

app.post('/api/usuarios',(req,res) => {
    const novoUsuario = {id: usuarios.length +1, nome: req.body.nome}

    usuarios.push(novoUsuario)

    res.status(201).json(novoUsuario)
})

app.get('/api/usuarios', (req, res) => {
    res.json(usuarios)
})

app.put('/api/usuarios/:id', (req, res) => 
{
    const usuario = usuarios.find(u => u.id === parseInt(req.params.id))

    if (!usuario) return res.status(404).send('Usuário não encontrado')

        usuario.nome = req.body.nome
        res.json(usuario)
})

app.delete('/api/usuarios/:id', (req, res) => {
    const usuarioIndex = usuarios.findIndex(u => u.id === parseInt(req.req.params.id))

    if(usuarioIndex === -1) return res.status(404).send('Usuário não encontrado')

    const usuarioDeletado = usuarios.splice(usuarioIndex,1)

    res.json(usuarioDeletado)
})
app.listen(PORT, () => {
    console.log(`Servidor rodando na porta https://localhost:${PORT}`)
})