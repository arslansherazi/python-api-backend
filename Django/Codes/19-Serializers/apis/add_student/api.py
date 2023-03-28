from Django.Codes.common.base_resource import BasePostResource
from apis.add_student.serializers import StudentSerializer
from models import StudentProfile


class AddStudent(BasePostResource):
    end_point = 'add_student'

    def insert_student_into_db(self):
        """
        Adds student into the system
        """
        try:
            student = StudentSerializer(data=self.request_args)
            if student.is_valid(raise_exception=True):
                student = student.save()
                if student:
                    student_profile_data = {}
                    for column, value in self.request_args.items():
                        student_profile_data[column] = value
                    StudentProfile.add_student_profile(student_id=student.id, **student_profile_data)
        except Exception as e:
            self.is_send_response = True
            self.response = {
                'message':  str(e)
            }

    def prepare_response(self):
        """
        Prepares response
        """
        self.response = {
            'data': {
                'is_student_added': True
            }
        }

    def process_request(self):
        """
        Process request
        """
        self.populate_request_arguments()
        self.insert_student_into_db()
        if self.is_send_response:
            return
        self.prepare_response()
