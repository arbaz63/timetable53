from django.shortcuts import render, redirect
from django import urls
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
import random

@api_view(['GET'])
def apiOverview(request):
    apiurls = {
        'Teachers\' List: /teacher_list/',
        'Add Teacher: /add_teacher/',
        'Edit Teacher: /edit_teacher/<str:pk>/',
        'Delete Teacher: /delete_teacher/<str:pk>/',
        'Departments\' list: /department_list/',
        'Add Department: /add_department/',
        'Edit Department: /edit_department/<str:pk>/',
        'Delete Department: /delete_department/<str:pk>/',
        'Courses\' list: /course_list/',
        'Add Course: /add_course/',
        'Edit Course: /edit_course/<str:pk>/',
        'Delete Course: /delete_course/<str:pk>/',
        'Sections\' List: /section_list/',
        'Add Section: /add_section/',
        'Edit Section: /edit_section/<str:pk>/',
        'Delete Section: /delete_section/<str:pk>/',
        'Rooms\' List: /room_list/',
        'Add Room: /add_room/',
        'Edit Room: /edit_room/<str:pk>/',
        'Delete Room: /delete_room/<str:pk>/',
        'Timeslots\' List: /timeslot_list/',
        'Add Timeslot: /add_timeslot/',
        'Edit Timeslot: /edit_timeslot/<str:pk>/',
        'Delete Timeslot: /delete_timeslot/<str:pk>/',
        'Timetables\' List: /timetable_list/',
        'Generate Classes: /generate_classes/<str:pk>',
        'Get Timetable: /get_timetable/<str:pk>',
        'Delete Timetable: /delete_timetable/<str:pk>',
    }
    return Response(sorted(apiurls))

@api_view(['GET'])
def teacherList(request):
    teachers = Teacher.objects.all()
    teacherSerializer = TeacherSerializer(teachers, many=True)
    return Response(teacherSerializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def addTeacher(request):
    teacherSerializer = TeacherSerializer(data=request.data)
    if teacherSerializer.is_valid():
        teacherSerializer.save()
        return Response(teacherSerializer.data, status=status.HTTP_200_OK)
    return Response("Failed to add the teacher", status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def editTeacher(request, pk):
    teacher = Teacher.objects.get(id=pk)
    teacherSerializer = TeacherSerializer(instance=teacher, data=request.data)
    if teacherSerializer.is_valid():
        teacherSerializer.save()
        return Response(teacherSerializer.data, status=status.HTTP_200_OK)
    return Response("Failed to edit the teacher", status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def deleteTeacher(request, pk):
    teacher = Teacher.objects.get(id=pk)
    teacher.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def departmentList(request):
    courses = Department.objects.all()
    departmentSerializer = DepartmentSerializer(courses, many=True)
    return Response(departmentSerializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def addDepartment(request):
    departmentSerializer = DepartmentSerializer(data=request.data)
    if departmentSerializer.is_valid():
        departmentSerializer.save()
        return Response(departmentSerializer.data, status=status.HTTP_200_OK)
    return Response("Failed to add the department", status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def editDepartment(request, pk):
    department = Department.objects.get(id=pk)
    departmentSerializer = DepartmentSerializer(instance=department, data=request.data)
    if departmentSerializer.is_valid():
        departmentSerializer.save()
        return Response(departmentSerializer.data, status=status.HTTP_200_OK)
    return Response("Failed to edit the department", status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def deleteDepartment(request, pk):
    department = Department.objects.get(id=pk)
    department.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def courseList(request):
    courses = Course.objects.all()
    courseSerializer = CourseSerializer(courses, many=True)
    return Response(courseSerializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def addCourse(request):
    courseSerializer = CourseSerializer(data=request.data)
    if courseSerializer.is_valid():
        courseSerializer.save()
        return Response(courseSerializer.data, status=status.HTTP_200_OK)
    return Response("Failed to add the course", status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def editCourse(request, pk):
    course = Course.objects.get(id=pk)
    courseSerializer = CourseSerializer(instance=course, data=request.data)
    if courseSerializer.is_valid():
        courseSerializer.save()
        return Response(courseSerializer.data, status=status.HTTP_200_OK)
    return Response("Failed to edit the department", status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteCourse(request, pk):
    course = Course.objects.get(id=pk)
    course.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def sectionList(request):
    sections = Section.objects.all()
    sectionSerializer = SectionSerializer(sections, many=True)
    return Response(sectionSerializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def addSection(request):
    sectionSerializer = SectionSerializer(data=request.data)
    if sectionSerializer.is_valid():
        sectionSerializer.save()
        return Response(sectionSerializer.data, status=status.HTTP_200_OK)
    return Response("Failed to add the section", status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def editSection(request, pk):
    section = Section.objects.get(id=pk)
    sectionSerializer = SectionSerializer(instance=section, data=request.data)
    if sectionSerializer.is_valid():
        sectionSerializer.save()
        return Response(sectionSerializer.data, status=status.HTTP_200_OK)
    return Response("Failed to edit the section", status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteSection(request, pk):
    section = Section.objects.get(id=pk)
    section.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def roomList(request):
    rooms = Room.objects.all()
    roomSerializer = RoomSerializer(rooms, many=True)
    return Response(roomSerializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def addRoom(request):
    roomSerializer = RoomSerializer(data=request.data)
    if roomSerializer.is_valid():
        roomSerializer.save()
        return Response(roomSerializer.data, status=status.HTTP_200_OK)
    return Response("Failed to add the room", status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def editRoom(request, pk):
    room = Room.objects.get(id=pk)
    roomSerializer = SectionSerializer(instance=room, data=request.data)
    if roomSerializer.is_valid():
        roomSerializer.save()
        return Response(roomSerializer.data, status=status.HTTP_200_OK)
    return Response("Failed to edit the room", status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    room.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def timeslotList(request):
    timeslots = Timeslot.objects.all()
    timeslotSerializer = TimeslotSerializer(timeslots, many=True)
    return Response(timeslotSerializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def addTimeslot(request):
    timeslotSerializer = TimeslotSerializer(data=request.data)
    if timeslotSerializer.is_valid():
        timeslotSerializer.save()
        return Response(timeslotSerializer.data, status=status.HTTP_200_OK)
    return Response(timeslotSerializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def editTimeslot(request, pk):
    timeslot = Timeslot.objects.get(id=pk)
    timeslotSerializer = TimeslotSerializer(instance=timeslot, data=request.data)
    if timeslotSerializer.is_valid():
        timeslotSerializer.save()
        return Response(timeslotSerializer.data, status=status.HTTP_200_OK)
    return Response(timeslotSerializer.data, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['DELETE'])
def deleteTimeslot(request, pk):
    timeslot = Timeslot.objects.get(id=pk)
    timeslot.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def timetableList(request):
    timetables = Timetable.objects.all()
    timetableSerializer = TimetableSerializer(timetables, many=True)
    return Response(timetableSerializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def addTimetable(request):
    timetableSerializer = TimetableSerializer(data=request.data)
    if timetableSerializer.is_valid():
        timetableSerializer.save()
        return Response(timetableSerializer.data, status=status.HTTP_200_OK)
    return Response("Failed to add the timetable", status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def generateClasses(request, pk):
    try:
        timetable = Timetable.objects.get(id=pk)
    except Timetable.DoesNotExist:
        return Response('Timetable does not exists', status=status.HTTP_400_BAD_REQUEST)
    department = timetable.department
    sections = Section.objects.filter(department=department)
    rooms = Room.objects.filter(department=department)
    timeslots = Timeslot.objects.filter(department=department)
    candidate_classes = []
    no_of_timeslots = len(timeslots)
    for section in sections:
        courses = section.courses.all()
        for course in courses:
            creditHours = course.creditHours
            for i in range(creditHours):
                print(course)
                inserted = False
                used_rooms = []
                all_rooms = rooms
                available_rooms = []
                checked_slots = set()
                while not inserted:
                    can_insert = True
                    timeslot = random.choice(timeslots)
                    checked_slots.add(timeslot)
                    classes_on_slot = Class.objects.filter(timeslot=timeslot,timetable=timetable)
                    for j in range(len(classes_on_slot)):
                        used_rooms.append(classes_on_slot[j].room)
                        if course.teacher == classes_on_slot[j].course.teacher or section == classes_on_slot[j].section:
                            can_insert = False
                            break
                    #checking if rooms are not availble in current timeslot
                    available_rooms = list(set(all_rooms) - set(used_rooms))
                    if len(available_rooms) == 0:
                        can_insert = False
                    if can_insert:
                        _class = Class(section=section, course=course, room=random.choice(available_rooms), timeslot=timeslot, timetable=timetable)
                        _class.save()
                        inserted = True
                        print(timeslot)
                    else:
                        used_rooms.clear()
                        #checking if all slots are checked and timetable is not completed
                        if len(checked_slots) == no_of_timeslots:
                            timetable.delete()
                            return Response("Failed to create the timetable", status=status.HTTP_400_BAD_REQUEST)
    classes = Class.objects.filter(timetable=pk)
    serializer = ClassSerializer(classes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)        

@api_view(['DELETE'])
def deleteTimetable(request, pk):
    timetable = Timetable.objects.get(id=pk)
    timetable.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def getTimetable(request, pk):
    classes = Class.objects.filter(timetable=pk)
    classSerializer = ClassSerializer(classes, many=True)
    return Response(classSerializer.data, status=status.HTTP_200_OK)