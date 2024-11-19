SELECT
    W.id,
    WP.age,
    W.coins_needed,
    W.power
FROM Wands W
LEFT JOIN Wands_Property WP ON W.code = WP.code
WHERE WP.is_evil = 0
AND (W.coins_needed, WP.age, W.power) IN (
    SELECT 
        MIN(W1.coins_needed),
        WP1.age,
        W1.power
    FROM Wands W1
    LEFT JOIN Wands_Property WP1 ON W1.code = WP1.code
    WHERE WP1.is_evil = 0
    GROUP BY WP1.age, W1.power
)
ORDER BY W.power DESC, WP.age DESC;
