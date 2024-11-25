SELECT 
    sup.*, 
    h.name 
FROM 
    Hackers h, 
    (
        SELECT 
            s.submission_date, 
            COUNT(DISTINCT s.hacker_id) AS counter,
            (
                SELECT 
                    s4.hacker_id 
                FROM 
                    Submissions s4 
                WHERE 
                    s4.submission_date = s.submission_date 
                GROUP BY 
                    s4.submission_date, s4.hacker_id 
                ORDER BY 
                    COUNT(s4.submission_id) DESC, 
                    s4.hacker_id ASC 
                LIMIT 1
            ) AS hacker 
        FROM 
            Submissions s 
        WHERE 
            s.hacker_id IN (
                SELECT 
                    s2.hacker_id 
                FROM 
                    Submissions s2 
                WHERE 
                    s2.submission_date <= s.submission_date 
                    AND DATEDIFF(s.submission_date, '2016-03-01') + 1 = (
                        SELECT 
                            COUNT(DISTINCT s3.submission_date) 
                        FROM 
                            Submissions s3 
                        WHERE 
                            s3.hacker_id = s2.hacker_id 
                            AND s3.submission_date <= s.submission_date 
                        GROUP BY 
                            s3.hacker_id
                    )
                GROUP BY 
                    s2.hacker_id
            ) 
        GROUP BY 
            s.submission_date
    ) sup 
WHERE 
    sup.hacker = h.hacker_id 
ORDER BY 
    sup.submission_date ASC;

