
from django.urls import path
from .import views

urlpatterns = [

    path('',views.index, name='index'),
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
    #path('form1/',views.form1, name='form1'),
    path('submit/',views.submit, name='submit'),
    path('form/', views.person_create_view, name='form_page'),
    path('<int:pk>/', views.person_update_view, name='person_change'),


    path('ajax/load-cities/', views.load_branches, name='ajax_load_branches'), # AJAX

]