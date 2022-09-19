db.students.drop():

db.students.insertOne([
    {"first_name": "john", "last_name": "Doe", "Student_id":1010}
])

my_query = { "Student_id": 1010 }

db.students.deleteOne(my_query)
