from django.urls import path
from .import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.drink_list, name='homepage'),
    path('<int:id>', views.drink_detail, name='=drinks_details'),
    path('members_page', views.member_list, name='members_page'),
    path('members_page/<int:id>', views.member_detail, name='members_detail'),
    path('courses_page', views.course_list, name='our_courses'),
    path('courses_page/<int:id>', views.course_details, name='courses_details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
