SELECT DISTINCT CITY FROM STATION 
WHERE NOT (
    LOWER(CITY) LIKE 'a%' OR
    LOWER(CITY) LIKE 'e%' OR
    LOWER(CITY) LIKE 'i%' OR
    LOWER(CITY) LIKE 'o%' OR
    LOWER(CITY) LIKE 'u%'
)