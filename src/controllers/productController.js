exports.createProduct = async (req, res) => {
    const { name, description, price, stock } = req.body;
    const newProduct = new Product({ name, description, price, stock });
    await newProduct.save();

    // Replication to backup server
    fetch('http://backup-server/api/products', { 
        method: 'POST', 
        headers: { 'Content-Type': 'application/json' }, 
        body: JSON.stringify(req.body) 
    });

    res.json(newProduct);
};
