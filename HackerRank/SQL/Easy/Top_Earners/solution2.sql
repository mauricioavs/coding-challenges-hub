SELECT
CONCAT(MAX(salary * months), '  ',COUNT(*))
FROM Employee
GROUP BY salary * months
ORDER BY salary * months DESC
LIMIT 1