import express from 'express'

const app = express()
const port = 3000

app.use(bodyParser.json())

app.use('/clientes', clienteRouter)

app.listen(port, () => {
    console.log(`Connected http://localhost:${port}`)
})