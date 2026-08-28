# Write your MySQL query statement below
SELECT 
    s.student_id,
    s.student_name,
    sub.subject_name,
    COUNT(e.subject_name) AS attended_exams
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN Examinations e
    ON s.student_id = e.student_id
    AND sub.subject_name = e.subject_name
GROUP BY 
    s.student_id,
    s.student_name,
    sub.subject_name
ORDER BY 
    s.student_id,
    sub.subject_name;

-- select s.student_id,s.student_name,sub.subject_name,
-- count(e.student_name) as attended_exams
-- from student s
-- cross join subject sub
-- left join examinations e on s.student_id = e.student_id
-- and sub.student_name = e.subject_name
-- group by s.student_id, s.student_name, sub.subject_name
-- order by s.student_id,
-- sub.subject_name;
