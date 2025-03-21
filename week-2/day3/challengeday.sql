CREATE TABLE product_orders (
    order_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    order_date TIMESTAMP DEFAULT NOW()
);

CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    order_id INT NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    price NUMERIC(10,2) NOT NULL CHECK (price >= 0),
    FOREIGN KEY (order_id) REFERENCES product_orders(order_id) ON DELETE CASCADE
);
 
CREATE FUNCTION get_total_order_price(order_id_param INT) 
RETURNS NUMERIC(10,2) AS $$
DECLARE 
    total_price NUMERIC(10,2);
BEGIN
    SELECT COALESCE(SUM(quantity * price), 0) INTO total_price -- 
    FROM items
    WHERE order_id = order_id_param;
    
    RETURN total_price;
END;
$$ LANGUAGE plpgsql;
 
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

ALTER TABLE product_orders 
ADD CONSTRAINT fk_product_orders_user 
FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE;
 
CREATE FUNCTION get_user_order_total(user_id_param INT, order_id_param INT) 
RETURNS NUMERIC(10,2) AS $$
DECLARE 
    total_price NUMERIC(10,2);
BEGIN
    SELECT COALESCE(SUM(quantity * price), 0) INTO total_price
    FROM items
    JOIN product_orders ON items.order_id = product_orders.order_id
    WHERE product_orders.user_id = user_id_param 
      AND product_orders.order_id = order_id_param;
    
    RETURN total_price;
END;
$$ LANGUAGE plpgsql;