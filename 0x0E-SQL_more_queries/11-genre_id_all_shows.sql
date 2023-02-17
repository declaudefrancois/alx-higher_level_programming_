-- lists all shows contained in hbtn_0d_tvshow.
SELECT t.title, t1.genre_id
FROM `tv_shows` AS t
LEFT JOIN `tv_show_genres` AS t1
ON t.id = t1.show_id
ORDER BY t.title ASC, t1.genre_id ASC;
