students = {
    1:{"name": "google", "age": 20},
    2:{"name": "Dell", "age": 22},
    3:{"name": "pwc", "age": 23},
    4:{"name": "aaa", "age": 24}
    }
for student_id,details in students.items():
        print(f"student_ID: {student_id}, Name: {details['name']}, Age: {details['age']}")