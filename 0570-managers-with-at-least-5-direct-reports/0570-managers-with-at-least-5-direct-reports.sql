-- Write your PostgreSQL query statement below
SELECT E.name
FROM Employee E JOIN 
    (SELECT E1.managerID 
    FROM Employee E1 
    GROUP BY E1.managerID 
    HAVING COUNT(E1.managerID) >= 5) E1
ON E.id = E1.managerId;