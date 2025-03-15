const express = require('express');
const http = require('http');
const path = require('path');

const app = express();
const server = http.createServer(app);

const PORT = 3001;

// Serve static files from the 'public' folder
app.use(express.static(path.join(__dirname, 'public')));

server.listen(PORT, () => {
    console.log(`🚀 Node.js server running at → http://localhost:${PORT}`);
});
