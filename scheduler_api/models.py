from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=50)
    creditHours = models.IntegerField()
    courseCode = models.CharField(max_length=10)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.name) + ' ' + str(self.teacher)

class Section(models.Model):
    name = models.CharField(max_length=10)
    courses = models.ManyToManyField(Course)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Timeslot(models.Model):
    day = models.CharField(max_length=10)
    timing = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('timing', 'day', 'department'),)
        ordering = ['department', 'day', 'timing']

    def __str__(self):
        return str(self.day) + ': ' + str(self.timing) + ' ' + str(self.department)

class Timetable(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('name', 'department'),)

    def __str__(self):
        return str(self.name) + ' ' + str(self.department)

class Class(models.Model):
    section = models.ForeignKey(Section,on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    timeslot = models.ForeignKey(Timeslot, on_delete=models.CASCADE)
    timetable = models.ForeignKey(Timetable, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'Classes'
    
    def __str__(self):
        return str(self.timeslot) + ' ' + str(self.section) + ' ' + str(self.course) + ' ' + str(self.room)
