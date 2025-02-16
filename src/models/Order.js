const mongoose = require("mongoose");

const orderSchema = new mongoose.Schema({
    user: { type: String, required: true },
    products: [{ productId: String, quantity: Number }],
    totalAmount: { type: Number, required: true },
    status: { type: String, enum: ["pending", "shipped", "delivered"], default: "pending" }
});

module.exports = mongoose.model("Order", orderSchema);
