--  lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT c.id, c.state_id, c.name
FROM `cities` AS c, `states` AS s
WHERE  s.name = "California"
       AND c.state_id = s.id
ORDER BY c.id ASC;
