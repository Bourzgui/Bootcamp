
SELECT * FROM customer;

SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM customer;

SELECT DISTINCT create_date FROM customer;

SELECT * FROM customer ORDER BY first_name DESC;

SELECT film_id, title, description, release_year, rental_rate 
FROM film 
ORDER BY rental_rate ASC;

SELECT address, phone 
FROM address 
WHERE district = 'Texas';

SELECT * FROM film WHERE film_id IN (15, 150);

SELECT film_id, title, description, length, rental_rate 
FROM film 
WHERE title = 'Inception';

SELECT film_id, title, description, length, rental_rate 
FROM film 
WHERE title LIKE 'In%';

-- 10. Trouver les 10 films les moins chers
SELECT film_id, title, rental_rate 
FROM film 
ORDER BY rental_rate ASC 
LIMIT 10;

SELECT film_id, title, rental_rate 
FROM film 
WHERE rental_rate > (SELECT MAX(rental_rate) 
                     FROM (SELECT rental_rate FROM film ORDER BY rental_rate ASC LIMIT 10) AS cheapest_movies)
ORDER BY rental_rate ASC 
LIMIT 10;

SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date 
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
ORDER BY c.customer_id ASC;

SELECT * 
FROM film 
WHERE film_id NOT IN (SELECT DISTINCT film_id FROM inventory);

SELECT city.city, country.country 
FROM city 
JOIN country ON city.country_id = country.country_id;

SELECT p.customer_id, c.first_name, c.last_name, p.amount, p.payment_date, p.staff_id 
FROM payment p
JOIN customer c ON p.customer_id = c.customer_id
ORDER BY p.staff_id;
