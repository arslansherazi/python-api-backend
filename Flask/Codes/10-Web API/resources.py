from app import api
from apis import StudentApis


# Resources
api.add_resource(StudentApis, '/api')