CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
);
 INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES ('Matt', 'Damon', '1970-10-08', 5);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES ('George', 'Clooney', '1961-05-06', 2);
 
  -- Ajouter la première actrice
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES ('Angelina', 'Jolie', '1975-06-04', 3);

-- Ajouter la deuxième actrice
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES ('Scarlett', 'Johansson', '1984-11-22', 1);


-- Ajouter trois autres acteurs en une seule requête
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES 
('Leonardo', 'DiCaprio', '1974-11-11', 1),
('Jennifer', 'Lawrence', '1990-08-15', 1),
('Brad', 'Pitt', '1963-12-18', 2);

SELECT * FROM actors

-- 1. Count how many actors are in the table
SELECT COUNT(*) AS total_actors
FROM actor;

-- 2. Try to add a new actor with some blank fields
INSERT INTO actor (first_name, last_name, birth_date)
VALUES ('', '', NULL);











