from django.urls import path
from apiapplication import views

urlpatterns = [
    path('student_register',views.StudentRegisterAPIView.as_view(),name="student_register"),
    path('login_show',views.LoginAPIView.as_view(),name='login_show'),
    # path('login_student',views.LoginAPIView.as_view(),name="login_student"),
    path('get_student',views.get_studentAPIView.as_view(),name='get_student'),
    path('single_student/<int:id>',views.singleStudentAPIView.as_view(),name='single_student'),
    path('delete_student/<int:id>',views.delete_studentAPIView.as_view(),name='delete_student'),
    path('update_student/<int:id>',views.update_studentAPIView.as_view(),name='update_student'),


]