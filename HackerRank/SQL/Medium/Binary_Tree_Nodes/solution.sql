SELECT
    N,
    CASE
    WHEN P is NULL THEN 'Root'
    WHEN EXISTS (
        SELECT 1
        FROM BST b2
        WHERE b2.P = b1.N 
    ) THEN 'Inner'
    ELSE 'Leaf'
    END
FROM BST b1
ORDER BY N