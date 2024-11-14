SET @a = (SELECT MIN(lat_n) FROM station);
SET @b = (SELECT MIN(long_w) FROM station);
SET @c = (SELECT MAX(lat_n) FROM station);
SET @d = (SELECT MAX(long_w) FROM station);

SELECT ROUND((ABS(@a - @c) + ABS(@b - @d)), 4)