SELECT
(CASE WHEN GR.GRADE >= 8 THEN ST.NAME ELSE NULL END),
GR.GRADE,
ST.MARKS
FROM STUDENTS ST
INNER JOIN GRADES GR ON ST.MARKS BETWEEN GR.MIN_MARK AND GR.MAX_MARK
ORDER BY GR.GRADE DESC, ST.NAME ASC, ST.MARKS ASC