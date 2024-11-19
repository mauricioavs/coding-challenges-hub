SELECT
hacker_id,
name,
SUM(max_challenge_score) AS total_challenge_score
FROM (
    SELECT
        H.hacker_id,
        H.name,
        MAX(score) AS max_challenge_score
    FROM Hackers H
    LEFT JOIN Submissions S ON H.hacker_id = S.hacker_id
    GROUP BY H.hacker_id, H.name, S.challenge_id
) AS HACKERS_WITH_CHALLENGE_SCORES
GROUP BY hacker_id, name HAVING total_challenge_score > 0
ORDER BY total_challenge_score DESC, hacker_id 
