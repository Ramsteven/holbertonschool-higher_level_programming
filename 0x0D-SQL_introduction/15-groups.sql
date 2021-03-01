-- Query that allow filter the duplicates
-- Show all duplicates with score and number
SELECT score, count(score) as number FROM second_table
       GROUP BY score
       ORDER BY score DESC;
