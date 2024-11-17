# Symmetric Pairs

**Platform**: HackerRank

**Category**: SQL

**Difficulty**: Medium

**URL**: https://www.hackerrank.com/challenges/symmetric-pairs/problem

## Problem Description

You are given a table, Functions, containing two columns: X and Y.

| Column | Type |
|-|-|
| X | Integer |
| Y | Integer |

Two pairs (X<sub>1</sub>, Y<sub>1</sub>) and (X<sub>2</sub>, Y<sub>2</sub>) are said to be symmetric pairs if X<sub>1</sub> = Y<sub>2</sub> and X<sub>2</sub> = Y<sub>1</sub>.

Write a query to output all such symmetric pairs in ascending order by the value of X. List the rows such that X<sub>1</sub> ≤ Y<sub>1</sub>.

Sample Input

| X | Y |
|-|-|
| 20 | 20 |
| 20 | 20 |
| 20 | 21 |
| 23 | 22 |
| 22 | 23 |
| 21 | 20 |

Sample Output

20 20  
20 21  
22 23  

## Solution

Refer to the `solution.sql` file in same directory for the solution.