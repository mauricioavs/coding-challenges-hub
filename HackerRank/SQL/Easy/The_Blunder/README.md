# The Blunder

**Platform**: HackerRank

**Category**: SQL

**Difficulty**: Easy

**URL**: https://www.hackerrank.com/challenges/the-blunder/problem

## Problem Description

Samantha was tasked with calculating the average monthly salaries for all employees in the EMPLOYEES table, but did not realize her keyboard's *0* key was broken until after completing the calculation. She wants your help finding the difference between her miscalculation (using salaries with any zeros removed), and the actual average salary.

Write a query calculating the amount of error (i.e.: *actual - miscalculated* average monthly salaries), and round it up to the next integer.

Input Format

The EMPLOYEES table is described as follows:

| Column | Type |
|-------|------|
| ID | Integer |
| Name | String |
| Salary | Integer |

Note: Salary is per month.

Constraints

*1000 < Salary < 10<sup>5</sup>*.

Sample Input

| ID | Name | Salary |
|-|-|-|
| 1 | Kristeen | 1420 |
| 2 | Ashley | 2006 |
| 3 | Julia | 2210 |
| 4 | Maria | 3000 |

Sample Output

2061

Explanation

The table below shows the salaries without zeros as they were entered by Samantha:

| ID | Name | Salary |
|-|-|-|
| 1 | Kristeen | 142 |
| 2 | Ashley | 26 |
| 3 | Julia | 221 |
| 4 | Maria | 3 |

Samantha computes an average salary of *98.00*. The actual average salary is *2159.00*.

The resulting error between the two calculations is *2159.00 - 98.00 = 2061.00*. Since it is equal to the integer *2061*, it does not get rounded up.

## Solution

Refer to the `solution.sql` file in same directory for the solution.