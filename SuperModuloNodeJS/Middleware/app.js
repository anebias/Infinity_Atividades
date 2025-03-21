// Primeiro importar o express
import express = require("express");
import { uuid } from "uuidv4";
import mongoose from "mongoose";

const mongoUri = "mongodb+srv://anebiasinfinity:QTGy03cz52qBFvGI@bancodadosaulanode.suwrv.mongodb.net/?retryWrites=true&w=majority&appName=BancoDadosAulaNode"

const connectDB = async()=>{
  try{
    await mongoose.connect(mongoUri,{
      useNewUrlParser: true,
      useUnifiedTopology: true
    })
  }
  catch(error){
  console.error('erro ao conectar',error)
  process.exit()
  }
}

connectDB()

// Inicializar o aplicativo express
const app = express();

// Definir a porta que o servidor vai rodar
let PORT = 3000;

// Lista de usuários
const lista_usuarios = [
    {
      id: 1,
      nome: "João Silva",
      email: "joao.silva@example.com"
    },
    {
      id: 2,
      nome: "Maria Oliveira",
      email: "maria.oliveira@example.com"
    },
    {
      id: 3,
      nome: "Carlos Souza",
      email: "carlos.souza@example.com"
    },
    {
      id: 4,
      nome: "Ana Costa",
      email: "ana.costa@example.com"
    },
    {
      id: 5,
      nome: "Felipe Almeida",
      email: "felipe.almeida@example.com"
    }
];
  
  console.log(lista_usuarios);

// Configurar o aplicativo para entender JSON no corpo das requisições
app.use(express.json());

// Criar middleware global

// Criar middleware local
const middlewareValidadorEmail = (req,res,next)=>{
    listaEmails=['@gmail.com','@hotmail.com','@outlook.com']

    const {email} = req.body.email
    function validarEmail(email){

        if(lista_usuarios.length>0){
            for (usuario of lista_usuarios){
                if(usuario.email !== email){
                    console.log('pode cadastrar')

                }else{next()}
        }

      
        }
    }
}


// Criar rotas 
app.post('/usuario/',(req,res)=>{
    const {nome, email, senha} = req.body
    const usuario = {
        id: uuid(),
        nome: nome,
        email: email,
        senha: senha
    };

    lista_usuarios.push(usuario)

    const retorno_usuario = {
        nome: nome,
        email: email,
    }

    res.status(201).json(retorno_usuario)
    console.log(`Usuário ${nome} criado`)
})

app.get('/usuario/:id',(req,res)=>{

    console.log(`Lista de usuários`)


})

// Inicializar o servidor na porta definida exibindo uma mensagem no console
app.listen(PORT,()=>{
    console.log(`Servidor rodando na porta http://localhost:${PORT}`)
});

// dontpad:
import express from 'express'
import { v4 as uuidv4 } from 'uuid';
import mongoose from 'mongoose';

const mongoUri= "mongodb+srv://luis98988:4jgxcFlUcbmyqBBX@cluster0.zxytv.mongodb.net/banco"
// mongodb+srv://luis98988:4jgxcFlUcbmyqBBX@cluster0.zxytv.mongodb.net/
const app = express()
const port = 3000

app.use(express.json())


const connectDB = async()=>{
    try{
        await mongoose.connect(mongoUri,{
            useNewUrlParser:true,
            useUnifiedTopology:true
        })
        console.log('O banco foi conectado com sucesso!!')
    }catch(error){
        console.error('erro ao conectar',error)
        process.exit()
    }
};

connectDB();

const lista_usuarios = []

//Global
app.use((req, res, next) => {

    console.log('middleware observando!!!')
    next()
})

//local
const middlewareVerificador = (req, res, next) => {
    const { senha } = req.body
    function verificar(senha) {
        if (senhas.includes(senha)) {
            console.log('senha confere')
            next()
        } else {
            res.status(401).josn({ error: 'Senha incorreta' })
        }
    }
    verificar(senha)
}

const middlewareValidadorEmail = (req, res, next) => {

    console.log(lista_usuarios.length)
    let { email } = req.body

    function validarEmail(email) {

        const emails = lista_usuarios.map(usuario => usuario.email)
        console.log(emails)
        if (emails.includes(email)) {
            res.status(403).json({ error: 'usaurio cadastrado' })
        } else {
            next()
        }
    }

    validarEmail(email)

}

app.post('/cadastrar-usuario', middlewareValidadorEmail, (req, res) => {
    const { nome, email, senha } = req.body
    const usuario = {
        id_usuario: uuidv4(),
        nome: nome,
        email: email,
        senha: senha
    }

    lista_usuarios.push(usuario)

    const retornoUser = {
        nome: nome,
        email: email
    }

    res.status(201).json(retornoUser)
})

app.get('/usuarios', (req, res) => {
    res.send(lista_usuarios)
})

app.put('/usuario/:id_usuario', (req, res) => {
    const { id_usuario } = req.params

    const { nome, email, senha } = req.body
    const usuario = lista_usuarios.findIndex(usuario => usuario.id_usuario === id_usuario)
    console.log(usuario)
    if (usuario === -1) {
        return res.status(404).json({ error: 'usuario não entrado' })
    }
    lista_usuarios[usuario] = { ...lista_usuarios[usuario], nome, email, senha }
    res.json(lista_usuarios[usuario])
})

app.delete('/usuario/:id_usuario', (req, res) => {
    const { id_usuario } = req.params
    const usuario = lista_usuarios.findIndex(usuario => usuario.id_usuario === id_usuario)

    if (usuario === -1) {
        return res.status(404).json({ error: 'usuario não entrado' })
    }


    lista_usuarios.splice(usuario, 1)
    res.json({ message: 'Usario removido com sucesso!!' })
})

app.listen(port, () => {
    console.log('servior rodadndo na porta', port)
})  