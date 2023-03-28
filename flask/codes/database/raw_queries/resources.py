from apis.add_student.api import AddStudent
from apis.delete_student.api import DeleteStudent
from apis.get_all_student.api import GetAllStudents
from apis.get_particular_student.api import GetParticularStudents
from apis.update_student.api import UpdateStudent
from app import api


# Resources
api.add_resource(AddStudent, '/apis/add_student')
api.add_resource(DeleteStudent, '/apis/delete_student')
api.add_resource(GetAllStudents, '/apis/get_all_students')
api.add_resource(GetParticularStudents, '/apis/get_student')
api.add_resource(UpdateStudent, '/apis/update_student')
