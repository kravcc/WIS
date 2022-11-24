from django.urls import path
from . import views

from django.contrib.auth.views import LoginView, LogoutView,PasswordChangeView,PasswordChangeDoneView



#basic
urlpatterns = [
    path('404', views.page404, name='page_404'),
    path('access_failed', views.access_failed, name='access_failed'),

    path('', views.index, name='index'),
    path('login', views.login_user, name='login'),
    path('logout',views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('study', views.study_view, name='study'),
    path('logged', views.logged_view, name='loggend_on'),
    path('profile', views.profile_view, name='profile'),
    path('profile_edit', views.profile_edit, name='profile_edit'),
    path('<int:id>', views.courses_view, name='courses-view'),
    path('admin_view', views.admin_view, name='admin_view'),
    path('user_update/<int:id>', views.user_update, name='user_update'),
    path('user_delete/<int:id>', views.user_delete, name='user_delete'),
    
    
    path('create-course',views.create_course, name='create_course'),
    
    path('get-courses-by-user-id/<int:id>',views.get_course_user,name='get_course_user'),

    path('garant_view', views.garant_view, name='garant_view'),
    path('student_list/<int:id>', views.students_view, name='student_list'),

    path('get-courses', views.get_courses, name='get_courses'),
    path('get-all-users/', views.get_users, name='get-all-users'),
    path('get-course-by-id/<int:id>', views.get_course_by_id, name='get_course-by-id'),
    path('get-logged-user', views.get_logged_user, name='get_logged_user'),


    path('add-user-to-course/<int:id_person>/<int:id_course>', views.add_user_to_course, name='add-user-to-course'),
    path('remove-user-from-course/<int:id_person>/<int:id_course>', views.remote_user_from_course, name='remove-user-from-course'),
]

handler404 = "main.views.page404"