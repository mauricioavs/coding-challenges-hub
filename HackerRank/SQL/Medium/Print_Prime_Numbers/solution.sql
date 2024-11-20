WITH RECURSIVE Numbers AS ( 
    SELECT 2 AS num 
    
    UNION ALL
    
    SELECT num + 1 
    FROM Numbers 
    WHERE num < 1000 
), 
nonprime AS ( 
    SELECT N1.num
    FROM Numbers N1
    JOIN Numbers N2 ON N2.num < N1.num AND N1.num % N2.num = 0 
) 

SELECT GROUP_CONCAT(num SEPARATOR '&') AS concatenated_value 
FROM Numbers
WHERE num NOT IN (SELECT num FROM nonprime)