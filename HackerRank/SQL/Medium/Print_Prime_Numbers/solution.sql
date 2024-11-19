WITH RECURSIVE PRIME_NUMBERS AS (
    SELECT 2 AS current_num
    
    UNION ALL

    (
        SELECT current_num+1
        FROM PRIME_NUMBERS PN
        WHERE NOT EXISTS(
            SELECT 1
            FROM PRIME_NUMBERS PN2
            WHERE MOD(current_num+1, PN2.current_num) = 0
        )
    ) OR 
    (
        SELECT NULL FROM PRIME_NUMBERS
        WHERE current_num <= 1000
    )
)

SELECT * FROM PRIME_NUMBERS