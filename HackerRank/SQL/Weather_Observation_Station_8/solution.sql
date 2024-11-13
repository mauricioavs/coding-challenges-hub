/*Solution 1*/
SELECT DISTINCT CITY FROM STATION
WHERE (
        LOWER(CITY) LIKE 'a%' OR
        LOWER(CITY) LIKE 'e%' OR
        LOWER(CITY) LIKE 'i%' OR
        LOWER(CITY) LIKE 'o%' OR
        LOWER(CITY) LIKE 'u%'
    )
    AND
    (
        LOWER(CITY) LIKE '%a' OR
        LOWER(CITY) LIKE '%e' OR
        LOWER(CITY) LIKE '%i' OR
        LOWER(CITY) LIKE '%o' OR
        LOWER(CITY) LIKE '%u'
    )
/*Solution 2*/
select distinct city from station where city regexp '^[AEIOUaeiou].*[AEIOUaeiou]$';