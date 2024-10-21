-- Write your PostgreSQL query statement below
SELECT id
FROM Weather W1
WHERE W1.temperature > (
    SELECT temperature
    FROM Weather W2
    WHERE W2.recordDate = W1.recordDate - INTERVAL '1 day'
);