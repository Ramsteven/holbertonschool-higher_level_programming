-- Querry tha show all records of database
-- List recors without empty name
SELECT * FROM second_table WHERE name IS NOT NULL ORDER BY score, name DESC;
