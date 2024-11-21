WITH Start_Dates AS (
    SELECT 
    Start_Date,
    ROW_NUMBER() OVER (ORDER BY Start_Date) AS RowNum
    FROM Projects
    WHERE Start_Date NOT IN (SELECT End_Date FROM Projects)
),
End_Dates AS (
    SELECT
    End_Date,
    ROW_NUMBER() OVER (ORDER BY End_Date) AS RowNum
    FROM Projects
    WHERE End_Date NOT IN (SELECT Start_Date FROM Projects)
)
SELECT 
    SD.Start_Date,
    ED.End_Date
FROM Start_Dates SD
LEFT JOIN End_Dates ED ON SD.RowNum = ED.RowNum
ORDER BY DATEDIFF(End_Date, Start_Date), Start_Date