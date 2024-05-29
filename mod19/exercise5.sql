SELECT students_groups.group_id,
        COUNT(DISTINCT students.student_id) AS number_students,
        SUM(assignments_grades.grade) as avg_grade,
        SUM(CASE WHEN assignments_grades.grade IS NULL THEN 1
                                                       ELSE 0 END) AS number_unsubmitted,
        SUM(CASE WHEN assignments.due_date < assignments_grades.date THEN 1
                                                                     ELSE 0 END) AS number_late_submitted,
        COUNT(assignments_grades.grade) AS number_retries
FROM students_groups
LEFT JOIN students ON students_groups.group_id = students.group_id
LEFT JOIN assignments ON students_groups.group_id = assignments.group_id
LEFT JOIN assignments_grades ON assignments.assisgnment_id = assignments_grades.assisgnment_id AND students.student_id = assignments_grades.student_id
GROUP BY students_groups.group_id;