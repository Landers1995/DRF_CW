from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitCreateAPIView, HabitDestroyAPIView,
                          HabitListAPIView, HabitRetrieveAPIView,
                          HabitUpdateAPIView, PublicListAPIView)

app_name = HabitsConfig.name

urlpatterns = [
    path("", HabitListAPIView.as_view(), name="habits"),
    path("public/", PublicListAPIView.as_view(), name="public"),
    path("create/", HabitCreateAPIView.as_view(), name="create"),
    path("retrieve/<int:pk>/", HabitRetrieveAPIView.as_view(), name="retrieve"),
    path("update/<int:pk>/", HabitUpdateAPIView.as_view(), name="update"),
    path("delete/<int:pk>/", HabitDestroyAPIView.as_view(), name="delete"),
]
