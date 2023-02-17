-- lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT t3.title
FROM `tv_genres` AS t, `tv_show_genres` AS t1, `tv_shows` AS t3
WHERE t.name = "Comedy" AND
      t1.genre_id = t.id AND
      t1.show_id = t3.id
ORDER BY t3.title ASC;
