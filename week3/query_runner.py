import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="sql_practice",
        user="rishika",
        host="localhost"
    )

def run_query(sql, params=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(sql, params)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def print_results(rows):
    for row in rows:
        print(row)

if __name__ == "__main__":
    
    print("--- Students above average GPA ---")
    rows = run_query("""
        SELECT name, branch, gpa
        FROM students
        WHERE gpa > (SELECT AVG(gpa) FROM students)
        ORDER BY gpa DESC
    """)
    print_results(rows)

    print("\n--- Branch averages ---")
    rows = run_query("""
        SELECT branch, ROUND(AVG(gpa), 2)
        FROM students
        GROUP BY branch
        ORDER BY 2 DESC
    """)
    print_results(rows)

    print("\n--- Students from a specific branch ---")
    branch ="AI & DE"
    rows=run_query("""
        SELECT name,gpa
        FROM students
        WHERE branch=%s
        ORDER BY gpa DESC
    """,params=(branch,))
    print_results(rows)
