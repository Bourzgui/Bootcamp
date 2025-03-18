SELECT * FROM customer;
 
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM customer;
 
SELECT DISTINCT create_date FROM customer;
 
SELECT * FROM customer ORDER BY first_name DESC;
 
SELECT film_id, title, description, release_year, rental_rate 
FROM film 
ORDER BY rental_rate ASC;

SELECT address, phone FROM address WHERE