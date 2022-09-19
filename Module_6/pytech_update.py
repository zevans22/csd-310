my_query = { "last_name": "james" }

new_values = { "$set": { "last_name": "white" } }

x = db.students.updateOne(my_query, new_values)

print (x.modified_count, "The last name of the Student with the ID 1007 has been changed to White.")
