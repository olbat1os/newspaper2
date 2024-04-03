from django.urls import path
from .views import PostDetailView, PostList

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetailView.as_view()),
]
