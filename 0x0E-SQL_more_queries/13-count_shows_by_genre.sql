-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT t.name AS genre, COUNT(t1.show_id) AS number_of_shows
FROM `tv_genres` AS t
INNER JOIN `tv_show_genres` AS t1
ON t.id = t1.genre_id
GROUP BY t.id
ORDER BY number_of_shows DESC, genre ASC;
