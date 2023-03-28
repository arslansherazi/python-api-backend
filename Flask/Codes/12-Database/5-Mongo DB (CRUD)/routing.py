from app import api
from apis import StudentApis


# routing
api.add_resource(StudentApis, '/student_apis')
