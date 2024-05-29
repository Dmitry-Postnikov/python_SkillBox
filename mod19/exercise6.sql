SELECT AVG(assignments_grades) AS avg_grade
FROM assignments
JOIN assignments_grades ON assignments.assisgnment_id = assignments_grades.assisgnment_id
WHERE assignments.assignment_text LIKE 'выучить%' OR assignments.assignment_text LIKE 'прочитать%'