from app import api
from apis import StudentApis, RefreshToken, GenerateToken

# Resources
api.add_resource(StudentApis, '/api')
api.add_resource(GenerateToken, '/api/token')
api.add_resource(RefreshToken, '/api/token/refresh')
