const express = require("express");
const dotenv = require("dotenv");
const cors = require("cors");
const bodyParser = require("body-parser");
const connectDB = require("./config/db");
const productRoutes = require('./routes/productRoutes');
const mongoose = require('mongoose');
const userRoutes = require('./routes/userRoutes'); // Ensure the path is correct


dotenv.config();
connectDB();

const app = express();
app.use(cors());
app.use(bodyParser.json());

// Routes
app.use("/api/products", require("./routes/productRoutes"));
// Middleware
app.use(express.json());
// Use Routes
app.use('/api/users', userRoutes);  // 👈 This must be present!
const PORT = process.env.PORT || 5001;
console.log("Using port:", PORT);
app.listen(PORT, () => console.log(`🚀 BackupServer running on port ${PORT}`));
app.get("/", (req, res) => {
    res.send("backup is running...");
  });
  