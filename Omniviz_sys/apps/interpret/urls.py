from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.interpret import views

urlpatterns = [
    path('api/upload', views.ImgUpload.as_view(), name='upload-api'),
    path('api/OD', views.OD_Interpret.as_view(), name='OD-api'),
    path('api/Seg', views.Seg_Interpret.as_view(), name='Seg-api'),
    path('api/CD', views.CD_Interpret.as_view(), name='CD-api'),
]