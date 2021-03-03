-- Import the database dump from hbtn_0d_tvshows to your MySQL server
-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
-- a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record displays: <TV Show genre> - <Number of shows linked to this genre>
-- First column is called genre
-- Second column is called number_of_shows
-- It won't display a genre that doesn’t have any shows linked
-- Results are sorted in descending order by the number of shows linked
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres JOIN tv_show_genres ON tv_genres.id=tv_show_genres.genre_id
GROUP BY tv_genres.name ORDER BY number_of_shows DESC