CREATE TABLE IF NOT EXISTS items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price INT NOT NULL
);

CREATE TABLE IF NOT EXISTS customers (
    id SERIAL PRIMARY KEY,
    firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL
);

INSERT INTO items (name, price) VALUES
('Small Desk', 100),
('Large Desk', 300),
('Fan', 80);

INSERT INTO customers (firstname, lastname) VALUES
('Greg', 'Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie', 'Johnson');

 SELECT * FROM items;

--SELECT * FROM items WHERE price > 80;

--SELECT * FROM items WHERE price <= 300;

--SELECT * FROM customers WHERE lastname = 'Smith';

--SELECT * FROM customers WHERE lastname = 'Jones';
 
--SELECT * FROM customers WHERE firstname <> 'Scott';







