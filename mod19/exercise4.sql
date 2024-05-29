SELECT students_groups.group_id,
        AVG(overdue_task) AS avg_overdue_task,
        MAX(overdue_task) AS max_overdue_task,
        MIN(overdue_task) AS min_overdue_task
FROM students_groups
JOIN (
    SELECT assignments.group_id, COUNT (CASE WHEN assignments.due_date < CURRENT_DATE THEN 1
                                                                                      ELSE NULL END) AS overdue_task
    FROM assignments
    GROUP BY assignments.group_id)
AS count_overdue ON students_groups.group_id = count_overdue.group_id
GROUP BY students_groups.group_id;