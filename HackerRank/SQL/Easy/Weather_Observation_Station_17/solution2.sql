SELECT ROUND(LONG_W, 4) FROM STATION 
WHERE LAT_N = (SELECT MIN(LAT_N) FROM STATION WHERE 38.778 < LAT_N)