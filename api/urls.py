from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('courses', views.CourseViewSet)
router.register('users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/course/<int:course_id>/', views.register_for_course, name='course_register'),
    path('api/token/', views.obtain_jwt_token, name='obtain_jwt_token')
]


