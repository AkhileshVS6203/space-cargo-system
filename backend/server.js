const express = require('express');
const path = require('path');
const app = express();

// Middleware
app.use(express.json());

// Example API route (optional)
app.get('/api/hello', (req, res) => {
  res.json({ message: 'Hello from backend! 🚀' });
});

// Serve frontend static files
app.use(express.static(path.join(__dirname, '../frontend/build')));

// Catch-all route for React
app.get('/*', (req, res) => {
  res.sendFile(path.join(__dirname, '../frontend/build/index.html'));
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`✅ Server is running at http://localhost:${PORT}`);
});
