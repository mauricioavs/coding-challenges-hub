# Contest Leaderboard

**Platform**: HackerRank

**Category**: SQL

**Difficulty**: Medium

**URL**: https://www.hackerrank.com/challenges/contest-leaderboard/problem

## Problem Description

You did such a great job helping Julia with her last coding contest challenge that she wants you to work on this one, too!

The total score of a hacker is the sum of their maximum scores for all of the challenges. Write a query to print the hacker_id, name, and total score of the hackers ordered by the descending score. If more than one hacker achieved the same total score, then sort the result by ascending hacker_id. Exclude all hackers with a total score of *0* from your result.

Input Format

The following tables contain contest data:

* Hackers: The hacker_id is the id of the hacker, and name is the name of the hacker.

| Column | Type |
|-|-|
| hacker_id | Integer |
| Name | String |

* Submissions: The submission_id is the id of the submission, hacker_id is the id of the hacker who made the submission, challenge_id is the id of the challenge for which the submission belongs to, and score is the score of the submission.

| Column | Type |
|-|-|
| submission_id | Integer |
| hacker_id | Integer |
| challenge_id | Integer |
| Score | Integer |

Sample Input

Hackers Table:

| hacker_id | name |
|-|-|
| 4071 | Rose |
| 4086 | Angela |
| 26071 | Frank |
| 49438 | Patrick |
| 74842 | Lisa |
| 80305 | Kimberly |
| 84072 | Bonnie |
| 87868 | Michael |
| 92118 | Todd |
| 95895 | Joe |

Submissions Table:

| submission_id | hacker_id | challenge_id | score |
|-|-|-|-|
| 67194 | 74842 | 63132 | 76 |
| 64479 | 74842 | 19797 | 98 |
| 40472 | 26071 | 49593 | 20 |
| 17513 | 4806 | 49593 | 20 |
| 69846 | 80305 | 19797 | 19 |
| 41002 | 26071 | 89343 | 36 |
| 52826 | 49438 | 49593 | 9 |
| 31093 | 26071 | 19797 | 2 |
| 81614 | 84072 | 49593 | 100 |
| 44829 | 26071 | 89343 | 17 |
| 75147 | 80305 | 49593 | 48 |
| 14115 | 4806 | 49593 | 76 |
| 6943 | 4071 | 19797 | 95 |
| 12885 | 4806 | 25917 | 13 |
| 73343 | 80305 | 49593 | 42 |
| 84264 | 84072 | 63132 | 0 |
| 9951 | 4071 | 49593 | 43 |
| 45104 | 49438 | 25917 | 34 |
| 53795 | 74842 | 19797 | 5 |
| 26363 | 26071 | 19797 | 29 |
| 10063 | 4071 | 49593 | 96 |

Sample Output

4071 Rose 191  
74842 Lisa 174  
84072 Bonnie 100  
4806 Angela 89  
26071 Frank 85  
80305 Kimberly 67  
49438 Patrick 43  

Explanation

Hacker 4071 submitted solutions for challenges 19797 and 49593, so the total score *=95+max(43,96)=191*.

Hacker 74842 submitted solutions for challenges 19797 and 63132, so the total score *max(98,5)+76=174*

Hacker 84072 submitted solutions for challenges 49593 and 63132, so the total score *=100+0=100*.

The total scores for hackers 4806, 26071, 80305, and 49438 can be similarly calculated.



## Solution

Refer to the `solution.sql` file in same directory for the solution.