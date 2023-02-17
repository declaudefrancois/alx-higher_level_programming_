-- lists all genres of the show Dexter.
SELECT t.name
FROM `tv_genres` AS t, `tv_show_genres` AS t1, `tv_shows` AS t3
WHERE t3.title = "Dexter" AND
      t1.genre_id = t.id AND
      t1.show_id = t3.id
ORDER BY t.name ASC;
