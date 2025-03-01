const express = require('express')
const app = express()
const PORT = 3000

app.use(express.json())

let biblioteca = [
    {
        "id": 101,
        "titulo": "O Grande Gatsby",
        "autor": "F. Scott Fitzgerald",
        "ano": 1925
      },
      {
        "id": 102,
        "titulo": "1984",
        "autor": "George Orwell",
        "ano": 1949
      },
      {
        "id": 103,
        "titulo": "Dom Quixote",
        "autor": "Miguel de Cervantes",
        "ano": 1605
      },
      {
        "id": 104,
        "titulo": "Cem Anos de Solidão",
        "autor": "Gabriel García Márquez",
        "ano": 1967
      },
      {
        "id": 105,
        "titulo": "A Moreninha",
        "autor": "Joaquim Manuel de Macedo",
        "ano": 1844
      }
    ] 

app.post('/api/livro',(req, res) => {
    const novoLivro = 
        {
            "id": biblioteca.length + 1,
            "titulo": req.body.titulo,
            "autor": req.body.autor,
            "ano": req.body.ano
          }

    biblioteca.push(novoLivro)

    res.status(201).json(novoLivro)
})

app.get('/api/livro', (req,res) => {

  res.json(biblioteca)

})

app.get('/api/livro/:id', (req, res) => {
  const livro = biblioteca.find(u => u.id === parseInt(req.params.id))

  if (!livro){
    return res.status(404).send('Não encontrado')
  }

  res.status(200).json(livro)

})

app.put('/api/livro/:id', (req, res) => {
  const livro = biblioteca.find(u => u.id === parseInt(req.params.id))

  if (!livro){
    return res.status(404).send('Não encontrado')
  }

  livro.titulo = req.body.titulo
  livro.autor = req.body.autor
  livro.ano = req.body.ano

  res.json(livro)
})

app.delete('/api/livro/:id', (req, res) => {
  const livroIndex = biblioteca.findIndex(u => u.id === parseInt(req.params.id))

  if (livroIndex == -1){
    return res.status(404).send('Não encontrado')
  }

  biblioteca.splice(livroIndex,1)

  res.status(200).json(biblioteca)

})

app.listen(PORT, () => 
{
  console.log(`Servidor rodando na porta ${PORT}`)
})