SELECT
S.submission_date,
COUNT(*) AS submissions_num,
S.hacker_id,
ROW_NUMBER() OVER (PARTITION BY S.submission_date ORDER BY S.hacker_id) AS RowNum
FROM Submissions S
GROUP BY submission_date, hacker_id HAVING (submission_date, COUNT(*)) IN (
    SELECT
    S1.submission_date,
    MAX(submissions_num) AS max_hacker_submission_num
    FROM (
        SELECT
        submission_date,
        hacker_id,
        COUNT(*) AS submissions_num
        FROM Submissions
        GROUP BY submission_date, hacker_id
    ) AS S1
    LEFT JOIN Hackers H ON S1.hacker_id = H.hacker_id
    GROUP BY submission_date
)
ORDER BY submission_date, hacker_id
