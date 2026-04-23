from .models import Users, Schedule, Grades, Subjects, Attendance, Payment
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username', 'email', 'student_class', 'is_active', 'is_staff', 'avatar']
        read_only_fields = ['id']
    
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username', 'email', 'student_class', 'is_active', 'is_staff', 'avatar']
        

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule 
        fields = [
            'id',
            'subject',
            'date',
            'start_time',
            'end_time',
            'classroom',
            'teacher',
            'class_name'
    ]
        



class GradesSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.username', read_only=True)
    subject_name = serializers.CharField(source='subject.name', read_only=True)
    class Meta:
        model = Grades 
        fields = [
            'id',
            'student',
            'subject',
            'student_name',
            'subject_name',
            'date',
            'grade',
            'lesson_topic',
    ]



class AttendanceSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.username', read_only=True)
    subject_name = serializers.CharField(source='subject.name', read_only=True)
    class Meta:
        model = Attendance
        fields = [
            'id',
            'student',
            'subject',
            'student_name',
            'subject_name',
            'date',
            'attendance'
    ]


class PaymentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.username', read_only=True)
    class Meta:
        model = Payment
        fields = [
            'id',
            'student',
            'student_name',
            'date_pay',
            'month',
            'paid'
    ]