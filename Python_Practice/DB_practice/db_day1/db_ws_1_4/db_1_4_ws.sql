CREATE TABLE users (
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);

SELECT
  first_name, phone, country
FROM
  users
WHERE
  phone LIKE '%-51__-%' AND country != '서울';

