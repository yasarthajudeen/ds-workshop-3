const express = require('express');
const router = express.Router();

// Define a valid route
router.get('/', (req, res) => {
  res.json({ message: 'Products API is working!' });
});

module.exports = router;
