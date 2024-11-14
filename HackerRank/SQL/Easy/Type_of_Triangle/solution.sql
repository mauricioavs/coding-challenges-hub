SELECT 
CASE
WHEN 2*GREATEST(A, B, C) >= A+B+C THEN 'Not A Triangle'
WHEN A=B AND B=C THEN 'Equilateral'
WHEN A=B OR B=C OR A=C THEN 'Isosceles'
ELSE 'Scalene'
END AS type_of_triangle
FROM TRIANGLES