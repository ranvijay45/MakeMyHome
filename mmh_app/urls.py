from django.urls import path
from .views import *

urlpatterns =[
    path('', home, name='home' ),
    path('owner_login/', owner_login, name="owner_login"),
    path('manager_login/', manager_login, name="manager_login"),
    path('owner_register/', owner_register, name="owner_register"),
    path('create-service-request/', create_service_request, name='create_service_request'),
    path('service-requests/', service_requests, name='service_requests'),
    path('logout/', logout, name="logout"),
    path('response/', response, name="response"),
    path('management/', management, name="management"),
    path('feedback/', feedback, name="feedback"),
    path('feedbacks/', feedbacks, name="feedbacks"),
    path('catalogue/<str:phone>/', catalogue, name='catalogue'),
    path('designs/<str:phone>/', design, name='designs'),
    path('projects/<str:phone>/', project, name='projects')
]