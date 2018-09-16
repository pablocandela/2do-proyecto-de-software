from aplicacion.models import User,Course,Take
from rest_framework import serializers
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','email','password','language','birthdate')

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id','teacher','title','description','level')

class TakeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Take
        fields = ('id','student','course','teacher_rating','student_rating')
