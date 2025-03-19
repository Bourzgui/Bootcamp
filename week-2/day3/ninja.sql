 
SELECT f.film_id, f.title, f.rating
FROM film f
LEFT JOIN rental r ON f.film_id = r.film_id
WHERE (f.rating IN ('G', 'PG')) 
AND (r.return_date IS NOT NULL OR r.rental_id IS NULL);
 
CREATE TABLE waiting_list (
    waiting_list_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customer(customer_id),
    film_id INT REFERENCES film(film_id),
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
 
SELECT f.title, COUNT(w.waiting_list_id) AS waiting_count
FROM film f
JOIN waiting_list w ON f.film_id = w.film_id
WHERE f.rating IN ('G', 'PG')
GROUP BY f.film_id, f.title
ORDER BY waiting_count DESC;
 
-- Ajouter des client 
INSERT INTO waiting_list (customer_id, film_id) VALUES
(1, 101),  
(2, 101), 
(3, 102);  
 