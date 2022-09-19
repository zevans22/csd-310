const database = 'pytech';
const collection = 'students';

use(database);
use('pytech');

db.students.drop();

db.students.insertMany([
{"Student_name": "zach", "Student_id": 1007},
{"Student_name": "bill", "Student_id": 1008},
{"Student_name": "jane", "Student_id": 1009},
]);
