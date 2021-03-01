-- Querry tha show all records of database
-- List recors without empty name
SELECT score, name FROM second_table WHERE TRIM(name) IS NOT NULL AND NOT name = '' ORDER BY score DESC;
