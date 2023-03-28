from django.contrib import admin

from students.models import Student, Semester


# registeration of models with admin site
admin.site.register(Student)
admin.site.register(Semester)
