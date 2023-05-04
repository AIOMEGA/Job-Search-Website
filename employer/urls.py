# from django.urls import include, path
# from courses import views

# app_name = 'courses'

# urlpatterns = [
#     path('', views.courses_view, name = 'courses'),
#     path('<int:pk>/', views.course_detail, name='course_detail'),
# ]

from django.urls import path
from . import views
from candidate import views as candidate_views
from employer import views as employer_views

app_name = 'employer'

urlpatterns = [
    path('', views.employer_home, name='home'),
    path('index/', views.index, name='index'),
    path('employer_profile/', views.employer_profile, name='profile'),
    path('jobs/', views.job_list, name='job_list'),
    path('job_post/', views.job_post, name='job_post'),
    path('signup/', views.employer_signup, name='employer_signup'),
    #path('signup/', employer_views.employer_signup, name='employer_signup'),
    path('employer_home/', views.employer_home, name='employer_home'),
    # other paths for employer app views
]