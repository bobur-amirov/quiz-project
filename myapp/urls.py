from django.urls import path, include

from  .views import quistion, qiuz, users_upload, result_list

urlpatterns = [
    path('', qiuz, name='qiuz'),
    path('quiz/<int:pk>/', quistion, name='quistion'),
    path('users/', users_upload, name='users-upload'),
    path('results/', result_list, name='results'),

]