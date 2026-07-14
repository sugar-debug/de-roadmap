import csv
import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="sql_practice",
        user="rishika",
        host="localhost"
    )


def create_table(cursor):
    cursor.execute("""
        DROP TABLE IF EXISTS students_new;
        CREATE TABLE students_new(
            name VARCHAR(50),
            age INT,
            branch VARCHAR(50),
            gpa DECIMAL(3,2),
            city VARCHAR(50)
        );
    """)
    print("Table created.")

def load_csv(cursor,filepath):
    with open (filepath,'r') as f:
        reader=csv.DictReader(f)
        for row in reader:
            cursor.execute("""
                INSERT INTO students_new (name,age,branch,gpa,city)
                VALUES (%s,%s,%s,%s,%s)
                """,(row['name'],row['age'],row['branch'],row['gpa'],row['city']))
    print("Data loaded.")

def query_results(cursor):
    cursor.execute("""
        SELECT name,branch,gpa
        FROM students_new
        ORDER BY gpa DESC;
    """)
    rows=cursor.fetchall()
    print("\n--- Loaded students ---")
    for row in rows:
        print(f"{row[0]:<12} {row[1]:<15} {row[2]:.2f}")



def run_pipeline():
    conn=None
    try:

        conn=get_connection()
        cursor=conn.cursor()

        create_table(cursor)
        load_csv(cursor,'week3/students_new.csv')
        query_results(cursor)
        
        conn.commit()
        print("Pipeline completed.")

    except Exception as e:
        print(f"\nPipeline failed :{e}")
        if conn:
            conn.rollback()
            print("Transaction rolled back.")

    finally:
        if conn:

            cursor.close()
            conn.close()
            print("Connection closed.")

if __name__=="__main__":
    run_pipeline()    
