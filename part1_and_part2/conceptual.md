### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
Relational database management system (RDMS)

- What is the difference between SQL and PostgreSQL?
SQL is a language, PSQL is a Relational database management system

- In `psql`, how do you connect to a database?
\c (db name)

- What is the difference between `HAVING` and `WHERE`?
HAVING: is used to check conditions after the aggregation takes place
WHERE: is used to check conditions before the aggregation takes place

- What is the difference between an `INNER` and `OUTER` join?
INNER join will give the intersecting data in the joined colums and OUTER join will give all the data

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
LEFT join will display all of the rows in the left table regardless if they have matching values in the right table, Right does the oposite 

- What is an ORM? What do they do?
ORM stands for Object-Relational Mapping. They allow you to manipulate data with an object oriented lanuage 

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
Client-Side:
You can do easily using AJAX libraries
Don’t have to involve Flask in the API
Can be faster: browser could talk directly to, say, Google Maps

Server Side: 
Same-Origin Policy may prevent browser requests
Easier to store and process data
Need password to access API

- What is CSRF? What is the purpose of the CSRF token?
A CSRF Token is a secret, unique and unpredictable value a server-side application generates in order to protect CSRF vulnerable resources. Kinda like a password that had to be input before any form data will be processed

- What is the purpose of `form.hidden_tag()`?
It generates a hidden field that includes a token that is used to protect the form against CSRF attacks.