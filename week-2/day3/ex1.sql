 
SELECT * FROM language;
SELECT 
    f.title,
    f.description,
    l.name AS language_name
FROM film f
INNER JOIN language l ON f.language_id = l.language_id;
SELECT 
    f.title,
    f.description,
    l.name AS language_name
FROM language l
LEFT JOIN film f ON l.language_id = f.language_id;

CREATE TABLE new_film (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

INSERT INTO new_film (name) VALUES
    ('The Matrix'),
    ('Inception'),
    ('Interstellar');

CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,
    film_id INTEGER NOT NULL,
    language_id SMALLINT NOT NULL,
    title VARCHAR(255) NOT NULL,
    score SMALLINT CHECK (score >= 1 AND score <= 10),
    review_text TEXT,
    last_update TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY (film_id) REFERENCES new_film(id) ON DELETE CASCADE,
    FOREIGN KEY (language_id) REFERENCES language(language_id)
);

INSERT INTO customer_review (film_id, language_id, title, score, review_text) VALUES
    (1, 1, 'Great Sci-Fi', 8, 'Really enjoyed the concepts in The Matrix'),
    (2, 1, 'Mind-bending', 9, 'Inception kept me guessing until the end');
 
 
DELETE FROM new_film WHERE id = 1;
When this runs, the review for 'The Matrix' (film_id = 1) will be automatically deleted from customer_review due to the ON DELETE CASCADE constraint. 