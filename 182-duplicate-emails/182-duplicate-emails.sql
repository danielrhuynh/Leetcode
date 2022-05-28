# Write your MySQL query statement below
SELECT DISTINCT Person.email FROM Person LEFT JOIN
(SELECT COUNT(email) AS counter, email, ID FROM Person GROUP BY email) duplicate 
ON Person.email = duplicate.email
WHERE duplicate.counter > 1