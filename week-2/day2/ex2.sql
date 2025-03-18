--1
SELECT * FROM customer;
--2
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM customer;
--3
SELECT DISTINCT create_date FROM customer;
--4
SELECT * FROM customer ORDER BY first_name DESC;
--5
SELECT film_id, title, description, release_year, rental_rate 
FROM film 
ORDER BY rental_rate ASC;
--6
SELECT address, phone 
FROM address 
WHERE district = 'Texas';
--7
SELECT * FROM film WHERE film_id IN (15, 150);
--8
SELECT film_id, title, description, length, rental_rate 
FROM film 
WHERE title = 'Inception';
--9
SELECT film_id, title, description, length, rental_rate 
FROM film 
WHERE title LIKE 'In%';

-- 10 
SELECT film_id, title, rental_rate 
FROM film 
ORDER BY rental_rate ASC 
LIMIT 10;
--11
SELECT film_id, title, rental_rate 
FROM film 
WHERE rental_rate > (SELECT MAX(rental_rate) 
                     FROM (SELECT rental_rate FROM film ORDER BY rental_rate ASC LIMIT 10) AS cheapest_movies)
ORDER BY rental_rate ASC 
LIMIT 10;
--12
SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date 
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
ORDER BY c.customer_id ASC;
--13
SELECT * 
FROM film 
WHERE film_id NOT IN (SELECT DISTINCT film_id FROM inventory);
--14
SELECT city.city, country.country 
FROM city 
JOIN country ON city.country_id = country.country_id;
--15
SELECT p.customer_id, c.first_name, c.last_name, p.amount, p.payment_date, p.staff_id 
FROM payment p
JOIN customer c ON p.customer_id = c.customer_id
ORDER BY p.staff_id;
