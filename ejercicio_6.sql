CREATE TABLE users (
  user_id INT PRIMARY KEY,
  user_name VARCHAR(255) NOT NULL
);

CREATE TABLE orders (
  order_id INT PRIMARY KEY,
  user_id INT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);



INSERT INTO users (user_id, user_name) VALUES
  (123, 'Bob'),
  (124, 'Alice'),
  (125, 'Carrie');

INSERT INTO orders (order_id, user_id) VALUES
  (123, 123),
  (111, 124),
  (666, 125);

  <-- Hacer Consultas-->

  SELECT u.user_id, u.user_name, o.order_id
FROM users AS u
LEFT JOIN orders AS o ON u.user_id = o.user_id;


SELECT *
FROM users AS a
RIGHT JOIN orders AS b
ON a.user_id = b.user_id;

SELECT
  u.user_id,
  u.user_name,
  o.order_id
FROM users AS u
FULL OUTER JOIN orders AS o
ON u.user_id = o.user_id;