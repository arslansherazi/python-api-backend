from mongoengine import Document, EmbeddedDocument, StringField, FloatField, EmbeddedDocumentField, ListField


class SemesterDetails(EmbeddedDocument):
    gpa = FloatField(required=True)
    major_subjects = ListField(required=True)


class Semesters(EmbeddedDocument):
    semester1 = EmbeddedDocumentField(SemesterDetails)
    semester2 = EmbeddedDocumentField(SemesterDetails)
    semester3 = EmbeddedDocumentField(SemesterDetails)
    semester4 = EmbeddedDocumentField(SemesterDetails)
    semester5 = EmbeddedDocumentField(SemesterDetails)
    semester6 = EmbeddedDocumentField(SemesterDetails)
    semester7 = EmbeddedDocumentField(SemesterDetails)
    semester8 = EmbeddedDocumentField(SemesterDetails)


class Student(Document):
    roll_no = StringField(required=True)
    name = StringField(required=True)
    degree = StringField(required=True)
    cgpa = FloatField(required=True)
    semesters_details = EmbeddedDocumentField(Semesters)

    meta = {
        'collection': 'students_data',  # if collection name is not specified then model name will be collection name
        'indexes': [{'fields': ['-roll_no'], 'unique': True}]
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
