import express from 'express';

const app = express();
const PORT = 3000;

app.get('/', (req, res) => 
    res.send(`PCT_news application is running on ${PORT}`)
)

app.listen(PORT, () =>
    console.log(`PCT_news server is running on port ${PORT}`)
)