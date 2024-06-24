-- Esta consulta lista todos los títulos de programas de televisión junto con sus IDs de género asociados, o 'NULL' si no tienen género.

SELECT tv_shows.title, COALESCE(tv_show_genres.id, 'NULL') AS id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, genre_id ASC;
