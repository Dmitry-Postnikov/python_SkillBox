SELECT students.full_name AS student_list
FROM students
JOIN students_groups ON students.group_id = students_groups.group_id
JOIN teachers ON students_groups.teacher_id = teachers.teacher_id
JOIN assignments ON teachers.teacher_id = assignments.teacher_id
JOIN (
    SELECT assignments.teacher_id, AVG(assignments_grades.grade) AS average_best_rating
    FROM assignments
    JOIN assignments_grades ON assignments.assisgnment_id = assignments_grades.assisgnment_id
    GROUP BY assignments.teacher_id)
AS teacher_average_best_rating ON teachers.teacher_id = teacher_average_best_rating.teacher_id
WHERE teacher_average_best_rating.average_best_rating = (
    SELECT MAX(average_best_rating)
    FROM (
        SELECT assignments.teacher_id, AVG(assignments_grades.grade) AS average_best_rating
        FROM assignments
        JOIN assignments_grades ON assignments.assisgnment_id = assignments_grades.assisgnment_id
        GROUP BY assignments.teacher_id
    )
AS max_average_best_rating
);