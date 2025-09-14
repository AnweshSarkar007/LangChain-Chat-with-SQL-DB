import sqlite3

## Connect to SQLite
connection = sqlite3.connect("student.db")

## Create a cursor object to create table and insert records
cursor = connection.cursor()

## Create the table
table_info="""
CREATE TABLE student(
    name VARCHAR(25),
    class VARCHAR(25),
    section VARCHAR(25),
    marks INT
)
"""

cursor.execute(table_info)

## Insert some more records
cursor.execute('''INSERT INTO student VALUES('Aayush', 'Data Science', 'A', 90)''')
cursor.execute('''INSERT INTO student VALUES('Maitree', 'Data Science', 'A', 100)''')
cursor.execute('''INSERT INTO student VALUES('Sundram', 'Data Science', 'B', 86)''')
cursor.execute('''INSERT INTO student VALUES('Avinash', 'Information Technology', 'A', 50)''')
cursor.execute('''INSERT INTO student VALUES('Tarush', 'Information Technology', 'A', 35)''')
cursor.execute('''INSERT INTO student VALUES('Rohan', 'Computer Science', 'A', 92)''')
cursor.execute('''INSERT INTO student VALUES('Priya', 'Data Science', 'B', 88)''')
cursor.execute('''INSERT INTO student VALUES('Ankit', 'Mechanical', 'C', 76)''')
cursor.execute('''INSERT INTO student VALUES('Neha', 'Electronics', 'A', 81)''')
cursor.execute('''INSERT INTO student VALUES('Karan', 'Civil', 'D', 69)''')
cursor.execute('''INSERT INTO student VALUES('Sonia', 'IT', 'B', 95)''')
cursor.execute('''INSERT INTO student VALUES('Vikram', 'AI', 'A', 99)''')
cursor.execute('''INSERT INTO student VALUES('Aditi', 'Biotech', 'C', 73)''')
cursor.execute('''INSERT INTO student VALUES('Manish', 'Computer Science', 'B', 84)''')
cursor.execute('''INSERT INTO student VALUES('Shreya', 'Data Science', 'D', 91)''')

cursor.execute('''INSERT INTO student VALUES('Rahul', 'Mechanical', 'A', 67)''')
cursor.execute('''INSERT INTO student VALUES('Sneha', 'AI', 'B', 90)''')
cursor.execute('''INSERT INTO student VALUES('Abhishek', 'IT', 'C', 85)''')
cursor.execute('''INSERT INTO student VALUES('Pooja', 'Electronics', 'A', 78)''')
cursor.execute('''INSERT INTO student VALUES('Dev', 'Civil', 'B', 64)''')
cursor.execute('''INSERT INTO student VALUES('Ishita', 'Data Science', 'C', 98)''')
cursor.execute('''INSERT INTO student VALUES('Sagar', 'Computer Science', 'D', 87)''')
cursor.execute('''INSERT INTO student VALUES('Meera', 'Biotech', 'A', 75)''')
cursor.execute('''INSERT INTO student VALUES('Arjun', 'Mechanical', 'C', 88)''')
cursor.execute('''INSERT INTO student VALUES('Nisha', 'AI', 'B', 94)''')

cursor.execute('''INSERT INTO student VALUES('Raj', 'Civil', 'A', 71)''')
cursor.execute('''INSERT INTO student VALUES('Komal', 'IT', 'B', 82)''')
cursor.execute('''INSERT INTO student VALUES('Yash', 'Electronics', 'D', 66)''')
cursor.execute('''INSERT INTO student VALUES('Tanvi', 'Computer Science', 'A', 97)''')
cursor.execute('''INSERT INTO student VALUES('Harsh', 'Biotech', 'C', 77)''')
cursor.execute('''INSERT INTO student VALUES('Kavya', 'Data Science', 'B', 89)''')
cursor.execute('''INSERT INTO student VALUES('Mohit', 'AI', 'D', 91)''')
cursor.execute('''INSERT INTO student VALUES('Simran', 'Mechanical', 'C', 72)''')
cursor.execute('''INSERT INTO student VALUES('Aditya', 'Civil', 'A', 83)''')
cursor.execute('''INSERT INTO student VALUES('Pallavi', 'IT', 'B', 92)''')

cursor.execute('''INSERT INTO student VALUES('Siddharth', 'Electronics', 'C', 80)''')
cursor.execute('''INSERT INTO student VALUES('Ritika', 'Computer Science', 'A', 96)''')
cursor.execute('''INSERT INTO student VALUES('Dhruv', 'Biotech', 'D', 68)''')
cursor.execute('''INSERT INTO student VALUES('Anjali', 'AI', 'C', 85)''')
cursor.execute('''INSERT INTO student VALUES('Varun', 'Data Science', 'B', 99)''')
cursor.execute('''INSERT INTO student VALUES('Mansi', 'Mechanical', 'A', 74)''')
cursor.execute('''INSERT INTO student VALUES('Aarav', 'Civil', 'C', 88)''')
cursor.execute('''INSERT INTO student VALUES('Sakshi', 'IT', 'D', 93)''')
cursor.execute('''INSERT INTO student VALUES('Akash', 'Electronics', 'B', 81)''')
cursor.execute('''INSERT INTO student VALUES('Divya', 'Computer Science', 'A', 90)''')

cursor.execute('''INSERT INTO student VALUES('Tejas', 'Biotech', 'C', 76)''')
cursor.execute('''INSERT INTO student VALUES('Radhika', 'AI', 'D', 95)''')
cursor.execute('''INSERT INTO student VALUES('Kunal', 'Mechanical', 'A', 70)''')
cursor.execute('''INSERT INTO student VALUES('Pritam', 'Civil', 'B', 62)''')
cursor.execute('''INSERT INTO student VALUES('Madhuri', 'IT', 'C', 84)''')
cursor.execute('''INSERT INTO student VALUES('Vishal', 'Data Science', 'D', 98)''')
cursor.execute('''INSERT INTO student VALUES('Ira', 'Electronics', 'A', 89)''')
cursor.execute('''INSERT INTO student VALUES('Omkar', 'Computer Science', 'B', 79)''')
cursor.execute('''INSERT INTO student VALUES('Payal', 'Biotech', 'C', 73)''')
cursor.execute('''INSERT INTO student VALUES('Ramesh', 'Mechanical', 'D', 65)''')

cursor.execute('''INSERT INTO student VALUES('Lavanya', 'Civil', 'A', 80)''')
cursor.execute('''INSERT INTO student VALUES('Tanya', 'AI', 'B', 91)''')
cursor.execute('''INSERT INTO student VALUES('Gaurav', 'Data Science', 'C', 97)''')
cursor.execute('''INSERT INTO student VALUES('Sana', 'IT', 'D', 82)''')
cursor.execute('''INSERT INTO student VALUES('Pranav', 'Electronics', 'A', 94)''')
cursor.execute('''INSERT INTO student VALUES('Bhavna', 'Computer Science', 'C', 88)''')
cursor.execute('''INSERT INTO student VALUES('Farhan', 'Biotech', 'B', 71)''')
cursor.execute('''INSERT INTO student VALUES('Mehul', 'Mechanical', 'D', 77)''')
cursor.execute('''INSERT INTO student VALUES('Rhea', 'Civil', 'A', 86)''')
cursor.execute('''INSERT INTO student VALUES('Zoya', 'AI', 'C', 92)''')

cursor.execute('''INSERT INTO student VALUES('Akhil', 'Data Science', 'B', 90)''')
cursor.execute('''INSERT INTO student VALUES('Natasha', 'IT', 'D', 78)''')
cursor.execute('''INSERT INTO student VALUES('Sameer', 'Electronics', 'A', 85)''')
cursor.execute('''INSERT INTO student VALUES('Jyoti', 'Mechanical', 'B', 66)''')
cursor.execute('''INSERT INTO student VALUES('Rajesh', 'Civil', 'C', 81)''')
cursor.execute('''INSERT INTO student VALUES('Alok', 'Computer Science', 'D', 93)''')
cursor.execute('''INSERT INTO student VALUES('Muskan', 'Biotech', 'A', 74)''')
cursor.execute('''INSERT INTO student VALUES('Naveen', 'AI', 'B', 88)''')
cursor.execute('''INSERT INTO student VALUES('Swati', 'Data Science', 'C', 99)''')
cursor.execute('''INSERT INTO student VALUES('Parth', 'Electronics', 'D', 90)''')

cursor.execute('''INSERT INTO student VALUES('Deepa', 'Mechanical', 'A', 79)''')
cursor.execute('''INSERT INTO student VALUES('Ashwin', 'Civil', 'B', 83)''')
cursor.execute('''INSERT INTO student VALUES('Harini', 'Computer Science', 'C', 95)''')
cursor.execute('''INSERT INTO student VALUES('Kabir', 'Biotech', 'A', 87)''')
cursor.execute('''INSERT INTO student VALUES('Monika', 'IT', 'D', 72)''')
cursor.execute('''INSERT INTO student VALUES('Sahil', 'AI', 'B', 97)''')
cursor.execute('''INSERT INTO student VALUES('Geeta', 'Data Science', 'C', 84)''')
cursor.execute('''INSERT INTO student VALUES('Suraj', 'Electronics', 'A', 89)''')
cursor.execute('''INSERT INTO student VALUES('Vidya', 'Civil', 'D', 75)''')
cursor.execute('''INSERT INTO student VALUES('Chirag', 'Computer Science', 'B', 91)''')

cursor.execute('''INSERT INTO student VALUES('Anusha', 'Mechanical', 'C', 67)''')
cursor.execute('''INSERT INTO student VALUES('Ishan', 'AI', 'A', 99)''')
cursor.execute('''INSERT INTO student VALUES('Reema', 'Data Science', 'B', 93)''')
cursor.execute('''INSERT INTO student VALUES('Krishna', 'IT', 'C', 81)''')
cursor.execute('''INSERT INTO student VALUES('Puneet', 'Biotech', 'D', 64)''')
cursor.execute('''INSERT INTO student VALUES('Smriti', 'Civil', 'A', 88)''')
cursor.execute('''INSERT INTO student VALUES('Arnav', 'Computer Science', 'B', 97)''')
cursor.execute('''INSERT INTO student VALUES('Shivani', 'Electronics', 'C', 77)''')
cursor.execute('''INSERT INTO student VALUES('Lakshya', 'Mechanical', 'D', 69)''')
cursor.execute('''INSERT INTO student VALUES('Gayatri', 'AI', 'A', 96)''')


## Display all the records
print("The inserted records are:")
data = cursor.execute('''SELECT * FROM student''')
for row in data:
    print(row)

## Commit your changes in the database
connection.commit()
connection.close()