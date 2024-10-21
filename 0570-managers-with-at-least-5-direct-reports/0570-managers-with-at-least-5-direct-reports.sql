-- Write your PostgreSQL query statement below
SELECT E.name
FROM Employee E
WHERE 5 <= (SELECT COUNT(E1.managerId) FROM Employee E1 WHERE E1.managerId = E.id);