from django.urls import path
from Serializers import views

app_name="Serializers"

urlpatterns = [
    path('',views.HelloAPIView.as_view(),name="Hello_API"),
    path('<int:pk>',views.HelloAPIView.as_view(),name="Hello_API1"),
]
