import time

from models import Student, StudentProfile, Course

from django.Codes.common.base_resource import BasePostResource


class GetStudentsInfo(BasePostResource):
    end_point = 'get_students_info'

    def initialize_class_attributes(self):
        """
        Initializes class attributes
        """
        self.students_profiles = {}
        self.select_related_profiles = {}
        self.students_courses = {}
        self.prefetch_related_courses ={}
        self.time_taken_by_getting_students_profiles = 0
        self.time_taken_by_getting_students_profiles_with_selected_related = 0
        self.time_taken_by_getting_students_courses = 0
        self.time_taken_by_getting_students_courses_with_prefetch_related = 0

    def get_student_profile(self):
        """
        Deletes order
        """
        start_time = time.time()
        self.students_profiles = StudentProfile.get_students_profiles()
        self.time_taken_by_getting_students_profiles = time.time() - start_time

        start_time = time.time()
        self.select_related_profile = StudentProfile.get_select_related_students_profiles()
        self.time_taken_by_getting_students_profiles_with_selected_related = time.time() - start_time

        start_time = time.time()
        self.students_courses = Course.get_students_courses()
        self.time_taken_by_getting_students_courses = time.time() - start_time

        start_time = time.time()
        self.prefetch_related_courses = Course.get_prefetch_related_students_courses()
        self.time_taken_by_getting_students_courses_with_prefetch_related = time.time() - start_time

    def prepare_response(self):
        """
        Prepares response
        """
        self.response = {
            'data': {
                'without_select_related': {
                    'time_taken': '{time} secs'.format(time=format(self.time_taken_by_getting_students_profiles, '.5f')),  # noqa: 501
                },
                'select_related': {
                    'time_taken': '{time} secs'.format(
                        time=format(self.time_taken_by_getting_students_profiles_with_selected_related, '.5f')
                    )
                },
                'without_prefetch_related': {
                    'time_taken': '{time} secs'.format(
                        time=format(self.time_taken_by_getting_students_courses, '.5f')),
                },
                'prefetch_related': {
                    'time_taken': '{time} secs'.format(
                        time=format(self.time_taken_by_getting_students_courses_with_prefetch_related, '.5f')
                    )
                },
            }
        }

    def process_request(self):
        """
        Process request
        """
        self.initialize_class_attributes()
        self.get_student_profile()
        self.prepare_response()
