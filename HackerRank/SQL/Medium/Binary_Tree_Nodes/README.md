# Binary Tree Nodes

**Platform**: HackerRank

**Category**: SQL

**Difficulty**: Medium

**URL**: https://www.hackerrank.com/challenges/binary-search-tree-1/problem

## Problem Description

You are given a table, BST, containing two columns: N and P, where N represents the value of a node in Binary Tree, and P is the parent of N.

| Column | Type |
|-|-|
| N | Integer |
| P | Integer |

Write a query to find the node type of Binary Tree ordered by the value of the node. Output one of the following for each node:

* Root: If node is root node.
* Leaf: If node is leaf node.
* Inner: If node is neither root nor leaf node.

Sample Input

| N | P |
|-|-|
| 1 | 2 |
| 3 | 2 |
| 6 | 8 |
| 9 | 8 |
| 2 | 5 |
| 8 | 5 |
| 5 | null |

Sample Output

1 Leaf  
2 Inner  
3 Leaf  
5 Root  
6 Leaf  
8 Inner  
9 Leaf  

Explanation

The Binary Tree below illustrates the sample:

```mermaid
graph TD;
  2 --> 1;
  2 --> 3;
  8 --> 6;
  8 --> 9;
  5 --> 2;
  5 --> 8;
  ```

## Solution

Refer to the `solution.sql` file in same directory for the solution.