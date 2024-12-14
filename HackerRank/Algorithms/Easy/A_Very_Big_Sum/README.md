# A Very Big Sum

**Platform**: HackerRank

**Category**: Algorithms

**Difficulty**: Easy

**URL**: https://www.hackerrank.com/challenges/a-very-big-sum/problem

## Problem Description

In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

Function Description

Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.

aVeryBigSum has the following parameter(s):

- int ar[n]: an array of integers .

Return

- long: the sum of all array elements

Input Format

The first line of the input consists of an integer .
The next line contains *n* space-separated integers contained in the array.

Output Format

Return the integer sum of the elements in the array.

Constraints

*1 &le; n &le; 10*  
*1 &le; ar[i] &le; 10<sup>10</sup>*

Sample Input
```
5
1000000001 1000000002 1000000003 1000000004 1000000005
```

Output
```
5000000015
```

Note:

The range of the 32-bit integer is *(-2<sup>31</sup>)* to *(2<sup>31</sup>)* or *[-2147483648, 2147483648]*.

When we add several integer values, the resulting sum might exceed the above range. You might need to use long int C/C++/Java to store such sums.

## Solution

Refer to the `solution.go` file in same directory for the solution.