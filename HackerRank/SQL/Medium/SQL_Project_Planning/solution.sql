SELECT
S.Name
FROM STUDENTS S
LEFT JOIN FRIENDS F ON S.ID = F.ID
LEFT JOIN PACKAGES P ON S.ID = P.ID
LEFT JOIN PACKAGES PF ON F.Friend_ID = PF.ID
where P.salary < PF.salary
ORDER BY PF.salary