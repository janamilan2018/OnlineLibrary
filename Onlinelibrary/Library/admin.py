from django.contrib import admin
from . models import (Student,PDF)

# Register your models here.

@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'dob','phone', 'email', 'password']

@admin.register(PDF)
class PDFModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'pdf']