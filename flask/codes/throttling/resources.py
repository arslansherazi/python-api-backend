from app import api
from apis import CompanyApis


# Resources
api.add_resource(CompanyApis, '/Company/api')
