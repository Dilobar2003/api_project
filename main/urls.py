from django.urls import path
from .views import HomeView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail' ),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='update' ),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete' )


]