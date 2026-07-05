-- Branches with average GPA above 8, rounded
SELECT branch, ROUND(AVG(gpa), 2)
FROM students
GROUP BY branch
HAVING AVG(gpa) > 8.00;


-- Students with no enrollments
SELECT s.name
FROM students s
LEFT JOIN enrollments e ON s.id = e.student_id
WHERE e.student_id IS NULL;


-- Count of students per performance category
SELECT
  CASE
    WHEN gpa >= 9.0 THEN 'Distinction'
    WHEN gpa >= 8.0 THEN 'First Class'
    WHEN gpa >= 7.0 THEN 'Second Class'
    ELSE 'Pass'
  END AS performance,
  COUNT(*) AS student_count
FROM students
GROUP BY performance;


-- Enrolled students from high-performing branches with grade labels
SELECT s.name, s.branch, e.course, e.grade,
  CASE
    WHEN e.grade IN ('A+', 'A') THEN 'Excellent'
    WHEN e.grade = 'B+' THEN 'Good'
    ELSE 'Average'
  END AS performance
FROM students s
INNER JOIN enrollments e ON s.id = e.student_id
WHERE s.branch IN (
    SELECT branch FROM students
    GROUP BY branch
    HAVING AVG(gpa) > 7.5
)
ORDER BY s.branch, e.grade DESC;


-- Students enrolled in a course AND above their own branch average GPA
SELECT s.name
FROM students s
JOIN enrollments e ON s.id = e.student_id
WHERE s.gpa > (
    SELECT AVG(s2.gpa)
    FROM students s2
    WHERE s2.branch = s.branch
);
