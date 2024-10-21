-- Write your PostgreSQL query statement below
SELECT St.student_id, St.student_name, Sb.subject_name,  COALESCE(COUNT(E.subject_name), 0) attended_exams 
FROM Students St CROSS JOIN Subjects Sb
LEFT JOIN Examinations E ON St.student_id = E.student_id AND Sb.subject_name = E.subject_name
GROUP BY St.student_id, St.student_name, Sb.subject_name
ORDER BY student_id, Sb.subject_name;