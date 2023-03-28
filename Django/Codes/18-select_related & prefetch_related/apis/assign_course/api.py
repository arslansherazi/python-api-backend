from models import Course

from Django.Codes.common.base_resource import BasePostResource


class AssignCourse(BasePostResource):
    end_point = 'assign_course'

    def populate_request_arguments(self):
        """
        Populates request arguments
        """
        self.course_id = self.request_args.get('course_id')
        self.student_id = self.request_args.get('student_id')

    def assign_course(self):
        """
        Assigns course to student
        """
        Course.assign_student_course(self.course_id, self.student_id)

    def prepare_response(self):
        """
        Prepares response
        """
        self.response = {
            'data': {
                'is_course_assigned': True
            }
        }

    def process_request(self):
        """
        Process request
        """
        self.populate_request_arguments()
        self.assign_course()
        self.prepare_response()
