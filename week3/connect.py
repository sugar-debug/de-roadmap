import psycopg2

conn = psycopg2.connect(
    dbname="sql_practice",
    user="rishika",
    host="localhost"
)

cursor = conn.cursor()

cursor.execute("SELECT name, gpa FROM students ORDER BY gpa DESC;")

rows = cursor.fetchall()

for row in rows:
    print(f"{row[0]:<10} GPA: {float(row[1]):.2f}")

cursor.close()
conn.close()
