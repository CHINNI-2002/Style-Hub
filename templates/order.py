<!DOCTYPE html>
<html>
<head>
    <title>Coin Order Form</title>
</head>
<body>
    <h1>Place Your Coin Order</h1>
    <form action="process_order.php" method="post">
        <label for="coin_type">Coin Type:</label>
        <input type="text" name="coin_type" id="coin_type" required><br>
        
        <label for="quantity">Quantity:</label>
        <input type="number" name="quantity" id="quantity" required><br>
        
        <label for="shipping_address">Shipping Address:</label>
        <textarea name="shipping_address" id="shipping_address" rows="4" required></textarea><br>
        
        <input type="submit" value="Place Order">
    </form>
</body>
</html>
