SELECT full_name, AVG(assignments_grades.grade) AS average_worst_rating
FROM teachers
JOIN assignments ON teachers.teacher_id
JOIN assignments_grades ON assignments.assisgnment_id = assignments_grades.assisgnment_id
GROUP BY full_name
ORDER BY average_worst_rating
LIMIT 1;