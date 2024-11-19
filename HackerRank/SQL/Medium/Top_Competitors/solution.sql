SELECT
S.hacker_id, H.name 
FROM SUBMISSIONS S
LEFT JOIN HACKERS H ON S.hacker_id = h.hacker_id
LEFT JOIN CHALLENGES C ON S.challenge_id = C.challenge_id
LEFT JOIN DIFFICULTY D ON C.difficulty_level = D.difficulty_level
WHERE S.score = D.score
GROUP BY S.hacker_id, name HAVING COUNT(*) > 1
ORDER BY COUNT(*) DESC, S.hacker_id