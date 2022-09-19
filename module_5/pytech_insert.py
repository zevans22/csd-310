const database = 'pytech';
const collection = 'students';

use(database);
use('pytech');

db.students.drop();

db.students.insertMany([
{"first_name": "zach", "last_name": "james", "Student_id": 1007},
{"first_name": "bill", "last_name": "brown", "Student_id": 1008},
{"first_name": "jane", "last_name": "king", "Student_id": 1009},
]);
