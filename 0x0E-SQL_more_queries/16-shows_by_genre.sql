-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT t.title, t2.name
FROM `tv_shows` AS t

LEFT JOIN `tv_show_genres` AS t1
ON t.id = t1.show_id

LEFT JOIN `tv_genres` AS t2
ON t2.id = t1.genre_id

ORDER BY t.title ASC;
