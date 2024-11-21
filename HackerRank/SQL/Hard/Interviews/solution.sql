SELECT
    SS.contest_id,
    SS.hacker_id,
    SS.name,
    SS.total_submissions,
    SS.total_accepted_submissions,
    VS.total_views,
    VS.total_unique_views
FROM (
    SELECT
        Contests.contest_id AS contest_id,
        Contests.hacker_id AS hacker_id,
        Contests.name AS name,
        SUM(Submission_Stats.total_submissions) AS total_submissions,
        SUM(Submission_Stats.total_accepted_submissions) AS total_accepted_submissions
    FROM Contests
    LEFT JOIN Colleges ON Contests.contest_id = Colleges.contest_id
    LEFT JOIN Challenges ON Colleges.college_id = Challenges.college_id
    LEFT JOIN Submission_Stats ON Challenges.challenge_id = Submission_Stats.challenge_id
    WHERE Submission_Stats.total_submissions + Submission_Stats.total_accepted_submissions > 0
    GROUP BY Contests.contest_id, Contests.hacker_id, Contests.name
) AS SS
LEFT JOIN (
    SELECT
        Contests.hacker_id AS hacker_id,
        SUM(View_Stats.total_views) AS total_views,
        SUM(View_Stats.total_unique_views) AS total_unique_views
    FROM Contests
    LEFT JOIN Colleges ON Contests.contest_id = Colleges.contest_id
    LEFT JOIN Challenges ON Colleges.college_id = Challenges.college_id
    LEFT JOIN View_Stats ON Challenges.challenge_id = View_Stats.challenge_id
    WHERE View_Stats.total_views + View_Stats.total_unique_views > 0
    GROUP BY Contests.hacker_id
) AS VS ON SS.hacker_id = VS.hacker_id
ORDER BY SS.contest_id
