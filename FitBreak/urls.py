from django.contrib import admin
from django.urls import path
from favorite import views
from fitnes.views import *
from pro_version.views import *

urlpatterns = [
    path('api/v1/favorite-exercises/', views.FavoriteExerciseListCreateAPIView.as_view()),
    path('api/v1/favorite-exercises/<int:id>/', views.FavoriteExerciseListCreateAPIView.as_view()),
    path('admin/', admin.site.urls),
    path('api/v1/eye/', training_eye),
    path('api/v1/hand/', training_hand),
    path('api/v1/neck/', training_neck),
    path('api/v1leg/', training_leg),
    path('api/v1/back/', training_back),
    path('api/v1/plusversion/', pro_version),
]