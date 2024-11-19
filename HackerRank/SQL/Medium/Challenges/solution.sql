WITH NUM_CHALLENGES AS(
    SELECT 
    H.hacker_id,
    H.name,
    COUNT(*) AS challenges_made
    FROM Hackers H
    LEFT JOIN Challenges C ON H.hacker_id = C.hacker_id
    GROUP BY H.hacker_id, H.name 
    ORDER BY H.hacker_id
)

SELECT * FROM NUM_CHALLENGES N1
WHERE challenges_made = (
    SELECT MAX(challenges_made)
    FROM NUM_CHALLENGES
)
OR
(
    SELECT COUNT(*)
    FROM NUM_CHALLENGES
    WHERE challenges_made = N1.challenges_made
) = 1
ORDER BY challenges_made DESC, hacker_id