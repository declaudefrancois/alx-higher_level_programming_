-- list all genres not linked to the show Dexter.
SELECT name FROM `tv_genres`
WHERE name NOT IN (
	SELECT t.name AS name
        FROM `tv_genres` AS t,
	     `tv_show_genres` AS t1,
	     `tv_shows` AS t2
	WHERE t.id = t1.genre_id AND
	      t1.show_id = t2.id AND
	      t2.title = "Dexter"
);
