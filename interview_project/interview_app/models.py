from django.db import models

class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    
    class Meta:
        app_label = 'interview_app'

class Class(models.Model):
    id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=255, unique=True)

class AssessmentArea(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255 , unique=True)

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=255 , unique=True)

class Answers(models.Model):
    id = models.AutoField(primary_key=True)
    answer = models.CharField(max_length=255, unique=True)

class Awards(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255 , unique=True)

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=255 , unique=True)
    subject_score = models.DecimalField(max_digits=5, decimal_places=2)

class Summary(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    syndey_participant = models.IntegerField()
    syndey_percentile = models.IntegerField()
    assessment_area = models.ForeignKey(AssessmentArea, on_delete=models.CASCADE)
    award = models.ForeignKey(Awards, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    correct_answer_percentage_per_class = models.DecimalField(max_digits=5, decimal_places=2)
    correct_answer = models.ForeignKey(Answers, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    student_score = models.DecimalField(max_digits=5, decimal_places=2)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    category_id = models.IntegerField()
    year_level_name = models.CharField(max_length=255)
