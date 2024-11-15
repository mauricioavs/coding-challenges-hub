WITH RECURSIVE pattern AS (
    SELECT 20 AS num
    UNION ALL
    SELECT num - 1 FROM pattern
    WHERE num > 1
)
SELECT REPEAT('* ', num) AS pattern_row
FROM pattern;