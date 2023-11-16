Make sure you download the starter code and run the following:

```sh
  psql < movies.sql
  psql movies_db
```

In markdown, you can place a code block inside of three backticks (```) followed by the syntax highlighting you want, for example

\```sql

SELECT \* FROM users;

\```

Using the `movies_db` database, write the correct SQL queries for each of these tasks:

1.  The title of every movie.
SELECT title FROM moveis;

2.  All information on the G-rated movies.
SELECT * FROM movies WHERE rating = 'G'

3.  The title and release year of every movie, ordered with the
    oldest movie first.
SELECT title, release_year FROM movies ORDER BY release_year DESC;

4.  All information on the 5 longest movies.
SELECT * FROM movies ORDER BY runtime DESC LIMIT 5;

5.  A query that returns the columns of `rating` and `total`, tabulating the
    total number of G, PG, PG-13, and R-rated movies.
SELECT rating, COUNT(rating) AS total FROM movies WHERE rating = 'G' OR rating = 'PG' OR rating = 'PG-13' OR rating = 'R' GROUP BY rating;

6.  A table with columns of `release_year` and `average_runtime`,
    tabulating the average runtime by year for every movie in the database. The data should be in reverse chronological order (i.e. the most recent year should be first).
SELECT AVG(runtime), release_year FROM movies GROUP BY release_year;

7.  The movie title and studio name for every movie in the
    database.
 SELECT title, name FROM movies JOIN studios ON movies.studio_id = studios.id;

8.  The star first name, star last name, and movie title for every
    matching movie and star pair in the database.
SELECT stars.first_name, stars.last_name, movies.title FROM roles INNER JOIN stars ON stars.id = roles.star_id
INNER JOIN movies ON movies.id = roles.movie_id;

9.  The first and last names of every star who has been in a G-rated movie. The first and last name should appear only once for each star, even if they are in several G-rated movies. *IMPORTANT NOTE*: it's possible that there can be two *different* actors with the same name, so make sure your solution accounts for that.
SELECT DISTINCT first_name, last_name, movies.rating FROM roles JOIN movies ON movies.id = roles.movie_id
JOIN stars ON stars.id = roles.star_id WHERE rating = 'G';

10. The first and last names of every star along with the number
    of movies they have been in, in descending order by the number of movies. (Similar to #9, make sure
    that two different actors with the same name are considered separately).
SELECT CONCAT(first_name, ' ', last_name) AS star_name, COUNT(title) AS movie_count FROM roles JOIN movies ON movies.id = roles.movie_id JOIN stars ON stars.id = roles.star_id GROUP BY first_name, last_name;
