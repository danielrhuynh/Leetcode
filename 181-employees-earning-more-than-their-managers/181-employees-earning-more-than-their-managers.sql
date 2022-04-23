# Write your MySQL query statement below
SELECT Employee.name AS "Employee" FROM Employee
LEFT JOIN
(SELECT id, name, salary FROM Employee) manager
ON Employee.managerId = manager.ID
WHERE Employee.salary > manager.salary