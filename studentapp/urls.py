from studentapp import views
from django.urls import path

from django.conf import settings
urlpatterns = [
    path('',views.addStudent,name='addStudent'),
    path('add_student_details',views.add_student_details,name='add_student_details'),
    path('show_students',views.show_students,name='show_students'),
    
    path('editpage/<int:bell>',views.editpage,name='editpage'),
    # path('deletepage/<int:bell>',views.deletepage,name='deletepage'),
    path('edit_student_details/<int:bell>',views.edit_student_details,name='edit_student_details'),
    path('delete_student/<int:bell>',views.delete_student,name='delete_student')

    
]

