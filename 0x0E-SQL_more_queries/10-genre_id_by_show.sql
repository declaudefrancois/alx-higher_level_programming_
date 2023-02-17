-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT t.title, t1.genre_id
FROM `tv_shows` AS t
INNER JOIN `tv_show_genres` AS t1
ON t.id = t1.show_id
ORDER BY t.title ASC, t1.genre_id ASC;
