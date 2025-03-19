 --Exe 1 : DVD Rentals
 
SELECT rental_id, customer_id, inventory_id, rental_date
FROM rental
WHERE return_date IS NULL;

SELECT customer.customer_id, customer.first_name, customer.last_name, COUNT(rental.rental_id) AS rentals_out
FROM rental
JOIN customer ON rental.customer_id = customer.customer_id
WHERE rental.return_date IS NULL
GROUP BY customer.customer_id, customer.first_name, customer.last_name
ORDER BY rentals_out DESC;
 
SELECT f.film_id, f.title 
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE a.first_name = 'Joe' AND a.last_name = 'Swank'
AND c.name = 'Action';
 
CREATE VIEW action_films_with_joe_swank AS 
SELECT f.film_id, f.title 
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE a.first_name = 'Joe' AND a.last_name = 'Swank'
AND c.name = 'Action';
 
SELECT * FROM action_films_with_joe_swank;
 
--Exe2  
 
SELECT s.store_id, c.city, co.country
FROM store s
JOIN address a ON s.address_id = a.address_id
JOIN city c ON a.city_id = c.city_id
JOIN country co ON c.country_id = co.country_id;
 
SELECT s.store_id, SUM(f.length) AS total_minutes
FROM inventory i
JOIN film f ON i.film_id = f.film_id
JOIN store s ON i.store_id = s.store_id
JOIN rental r ON i.inventory_id = r.inventory_id
WHERE r.return_date IS NOT NULL
GROUP BY s.store_id;
 
SELECT DISTINCT c.customer_id, c.first_name, c.last_name, ci.city
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
WHERE ci.city IN (
    SELECT city FROM city 
    JOIN address ON city.city_id = address.city_id
    JOIN store ON address.address_id = store.address_id
);

SELECT DISTINCT c.customer_id, c.first_name, c.last_name, co.country
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id
WHERE co.country IN (
    SELECT country FROM country 
    JOIN city ON country.country_id = city.country_id
    JOIN address ON city.city_id = address.city_id
    JOIN store ON address.address_id = store.address_id
);
 
SELECT film_id, title, length 
FROM film 
WHERE film_id NOT IN (
    SELECT film_id FROM film_category fc
    JOIN category c ON fc.category_id = c.category_id
    WHERE c.name = 'Horror'
)
AND title NOT ILIKE '%beast%' 
AND title NOT ILIKE '%monster%' 
AND title NOT ILIKE '%ghost%' 
AND title NOT ILIKE '%dead%' 
AND title NOT ILIKE '%zombie%' 
AND title NOT ILIKE '%undead%';

SELECT SUM(length) AS total_minutes, 
       ROUND(SUM(length) / 60.0, 2) AS total_hours, 
       ROUND(SUM(length) / 1440.0, 2) AS total_days
FROM film 
WHERE film_id NOT IN (
    SELECT film_id FROM film_category fc
    JOIN category c ON fc.category_id = c.category_id
    WHERE c.name = 'Horror'
)
AND title NOT ILIKE '%beast%' 
AND title NOT ILIKE '%monster%' 
AND title NOT ILIKE '%ghost%' 
AND title NOT ILIKE '%dead%' 
AND title NOT ILIKE '%zombie%' 
AND title NOT ILIKE '%undead%';
