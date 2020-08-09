import express, { Router } from 'express';
import mongoose from 'mongoose';

const app = express();
const PORT = 3000;

app.get('/', (req, res) => 
    res.send(`PCT_news application is running on ${PORT}`)
)

app.listen(PORT, () =>
    console.log(`PCT_news server is running on port ${PORT}`)
)

// npm start
// lsof -i:3000 
// kill -9 [PID] 