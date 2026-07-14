-- Window function: average GPA per branch alongside each student
SELECT name, branch, gpa,
  ROUND(AVG(gpa) OVER(PARTITION BY branch), 2) AS branch_avg
FROM students;

-- Window function: rank students within each branch
SELECT name, branch, gpa,
  RANK() OVER(PARTITION BY branch ORDER BY gpa DESC) AS rank_in_branch
FROM students;

-- Window function: combined branch avg and rank in one query
SELECT name, branch, gpa,
  ROUND(AVG(gpa) OVER(PARTITION BY branch), 2) AS branch_avg,
  RANK() OVER(PARTITION BY branch ORDER BY gpa DESC) AS rank_in_branch
FROM students;

-- CTE: students above overall average GPA
WITH cte_filter AS (
    SELECT name, gpa
    FROM students
    WHERE gpa > (SELECT AVG(gpa) FROM students)
)
SELECT * FROM cte_filter;

-- CTE: top ranked student per branch
WITH top_rankers AS (
    SELECT name, branch,
           RANK() OVER(PARTITION BY branch ORDER BY gpa DESC) AS rank_in_branch
    FROM students
)
SELECT name, branch
FROM top_rankers
WHERE rank_in_branch = 1;
