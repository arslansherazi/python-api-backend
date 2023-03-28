from django_mongoengine import Document, EmbeddedDocument, fields


class SemesterDetails(EmbeddedDocument):
    gpa = fields.FloatField(blank=False)
    major_subjects = fields.ListField(blank=False)


class Semesters(EmbeddedDocument):
    semester1 = fields.EmbeddedDocumentField(SemesterDetails)
    semester2 = fields.EmbeddedDocumentField('SemesterDetails')
    semester3 = fields.EmbeddedDocumentField('SemesterDetails')
    semester4 = fields.EmbeddedDocumentField('SemesterDetails')
    semester5 = fields.EmbeddedDocumentField('SemesterDetails')
    semester6 = fields.EmbeddedDocumentField('SemesterDetails')
    semester7 = fields.EmbeddedDocumentField('SemesterDetails')
    semester8 = fields.EmbeddedDocumentField('SemesterDetails')


class Student(Document):
    roll_no = fields.StringField(blank=False, primary_key=True)  # data with same primary key replace the previous data
    name = fields.StringField(blank=False)
    degree = fields.StringField(blank=False)
    cgpa = fields.FloatField(blank=False)
    semesters_details = fields.EmbeddedDocumentField('Semesters')

    meta = {
        'collection': 'students_data',  # if collection name is not specified then model name will be collection name
        'indexes': [{'fields': ['degree'], 'unique': False}]  # We cannot add primary_key column as index as it is already an index  # noqa: 501
    }

    def to_dict(self):
        semesters_details = {}
        for semester_name in self.semesters_details._data.keys():
            semester_detail = self.semesters_details._data.get(semester_name)
            semesters_details[semester_name] = {
                    'gpa': semester_detail.gpa,
                    'major_subjects': semester_detail.major_subjects
            }
        return {
            'name': self.name,
            'degree': self.degree,
            'cgpa': self.cgpa,
            'semesters_details': semesters_details
        }
