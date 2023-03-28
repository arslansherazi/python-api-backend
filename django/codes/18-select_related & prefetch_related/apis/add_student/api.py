from models import Student, StudentProfile

from django.codes.common.base_resource import BasePostResource


class AddStudent(BasePostResource):
    end_point = 'add_student'

    def populate_request_arguments(self):
        """
        Populates request arguments
        """
        self.roll_no = self.request_args.get('roll_no')
        self.current_semester = int(self.request_args.get('current_semester'))
        self.session_start = self.request_args.get('session_start')
        self.session_end = self.request_args.get('session_end')
        self.contact_no = self.request_args.get('contact_no')
        self.address = self.request_args.get('address')
        self.first_name = self.request_args.get('first_name')
        self.last_name = self.request_args.get('last_name')

    def insert_student_into_db(self):
        """
        Adds student into the system
        """
        student_id = Student.insert_student_into_db(
            self.roll_no, self.current_semester, self.session_start, self.session_end
        )
        StudentProfile.add_student_profile_into_db(
            student_id, self.address, self.first_name, self.last_name, self.contact_no
        )

    def prepare_response(self):
        """
        Prepares response
        """
        self.response = {
            'data': {
                'is_signed_up': True
            }
        }

    def process_request(self):
        """
        Process request
        """
        self.populate_request_arguments()
        self.insert_student_into_db()
        self.prepare_response()
