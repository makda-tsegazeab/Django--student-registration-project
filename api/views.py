from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import CourseSerializer, RegistrationSerializer, UserSerializer
from courses.models import Course
from registration.models import Registration
from users.models import User

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken

# Courses API (using generic viewset)
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]  # Add authentication here

# Registration API (using custom logic)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def register_for_course(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

    if Registration.objects.filter(student=request.user, course=course).exists():
        return Response({'error': 'Already registered for this course'}, status=status.HTTP_400_BAD_REQUEST)

    registration = Registration.objects.create(student=request.user, course=course)
    serializer = RegistrationSerializer(registration)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

# Users API (using generic viewset)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Adjust permissions as needed

    def create(self, request, *args, **kwargs):
        # Implement logic for creating a user with different roles (student/admin)
        # based on request data or user attributes
        return super().create(request, *args, **kwargs)


@api_view(['POST'])
def obtain_jwt_token(request):
    refresh = RefreshToken.for_user(request.user)
    token = str(refresh.access_token)
    return Response({'token': token})