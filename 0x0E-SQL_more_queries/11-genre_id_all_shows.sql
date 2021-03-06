-- Import the database dump from hbtn_0d_tvshows to your MySQL server
-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
-- a script that lists all shows contained in the database hbtn_0d_tvshows.
-- Each record displays: tv_shows.title - tv_show_genres.genre_id
-- Results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- If a show doesn’t have a genre, it will display NULL
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;