from models import Course

from django.codes.common.base_resource import BasePostResource


class AddCourse(BasePostResource):
    end_point = 'add_course'

    def populate_request_arguments(self):
        """
        Populates request arguments
        """
        self.code = self.request_args.get('code')
        self.name = self.request_args.get('name')

    def insert_course_into_db(self):
        """
        Adds course into the system
        """
        Course.add_course_into_db(self.code, self.name)

    def prepare_response(self):
        """
        Prepares response
        """
        self.response = {
            'data': {
                'is_course_added': True
            }
        }

    def process_request(self):
        """
        Process request
        """
        self.populate_request_arguments()
        self.insert_course_into_db()
        self.prepare_response()
