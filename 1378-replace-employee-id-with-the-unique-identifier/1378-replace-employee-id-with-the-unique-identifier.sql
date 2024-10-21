-- Write your PostgreSQL query statement below
SELECT unique_id, name
FROM EmployeeUNI LEFT JOIN Employees ON EmployeeUNI.id = Employees.id;