SELECT DISTINCT full_name, AVG(grade) AS average_best_rating
FROM students
JOIN assignments_grades ON students.student_id = assignments_grades.student_id
GROUP BY full_name
ORDER BY average_best_rating DESC
LIMIT 10;