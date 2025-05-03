import "dotenv/config" ;
import express from "express";
import {projetosRoutes} from './routes/projetos.js'
import {usuariosRoutes} from './routes/usuarios.js'
import {autenticacaoRoutes} from './routes/autenticacao.js'
import cors from 'cors'

console.log(process.env.DB_HOST); // "localhost"
console.log(process.env.DB_USER); // "root"

export const app = express();

// const projetos = [
//     { id: 0, titulo: "Primeiro projeto", descricao: "Meu primeiro projeto" },
//     { id: 1, titulo: "Segundo projeto", descricao: "Meu primeiro projeto" },
//     { id: 2, titulo: "Terceiro projeto", descricao: "Meu primeiro projeto" }
//   ]

app.use(express.json());

app.use(cors({
  origin: ["*"],
}))

// rota utilizada para disponibilizar a documentação
app.get('/',(req,res)=>{
    res.send({message: 'cheguei aqui...'})
});

app.use(projetosRoutes)
app.use(usuariosRoutes)
app.use(autenticacaoRoutes)