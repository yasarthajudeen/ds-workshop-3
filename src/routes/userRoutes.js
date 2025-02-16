const express = require('express');
const router = express.Router();

// Example Route (Modify based on your API)
router.get('/', (req, res) => {
    res.json({ message: "Users API is working!" });
});

module.exports = router;

