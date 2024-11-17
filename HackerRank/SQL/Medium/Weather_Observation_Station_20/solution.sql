SET @total_rows = (SELECT COUNT(*) FROM STATION);

WITH OrderedData AS (
    SELECT
        LAT_N,
        ROW_NUMBER() OVER (ORDER BY LAT_N) AS RowNum    
    FROM STATION
)

SELECT
    ROUND(AVG(LAT_N), 4)
FROM OrderedData
WHERE RowNum IN(@total_rows/2, @total_rows/2 + 1, (@total_rows + 1) / 2)