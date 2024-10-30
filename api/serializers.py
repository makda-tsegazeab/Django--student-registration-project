from rest_framework import serializers
from courses.models import Course
from registration.models import Registration
from users.models import User

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    student = serializers.SlugRelatedField(slug_field='username', read_only=True)
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Registration
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'