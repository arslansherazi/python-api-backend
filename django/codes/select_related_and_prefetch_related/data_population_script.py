import random
import uuid

import requests
from faker import Faker

faker = Faker()

def populate_students():
    for i in range(1, 10000):
        session_start = random.randint(2000, 2021)
        params = {
            'roll_no': str(uuid.uuid4()).split('-')[0],
            'current_semester': random.randint(1, 8),
            'session_start': str(session_start),
            'session_end': str(session_start + 4),
            'first_name': faker.first_name(),
            'last_name': faker.last_name(),
            'address': faker.address(),
            'contact_no': faker.phone_number()
        }
        requests.post('http://0.0.0.0:8001/database/add_student', data=params)
        print('student {id} is added'.format(id=i))


def populate_courses():
    for i in range(1, 1000):
        params = {
            'code': str(uuid.uuid4()).split('-')[1],
            'name': '{char_1}{char_2}{char_3}'.format(
                char_1=chr(random.randint(65, 90)),
                char_2=chr(random.randint(65, 90)),
                char_3=chr(random.randint(65, 90)),
            ),
        }
        requests.post('http://0.0.0.0:8001/database/add_course', data=params)
        print('course {id} is added'.format(id=i))


def assign_student_course():
    for i in range(1, 1000):
        for j in range(1, random.randint(1, 100)):
            params = {
                'course_id': i,
                'student_id': random.randint(1, 10000)
            }
            requests.post('http://0.0.0.0:8001/database/assign_course', data=params)
        print('course {id} is assigned'.format(id=i))


if __name__ == '__main__':
    populate_students()
    populate_courses()
    assign_student_course()
