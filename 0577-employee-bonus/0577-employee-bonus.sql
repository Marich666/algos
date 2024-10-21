-- Write your PostgreSQL query statement below
SELECT name, bonus      
FROM Bonus RIGHT JOIN Employee on Bonus.empId = Employee.empId
WHERE bonus < 1000 OR bonus is null;