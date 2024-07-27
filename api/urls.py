from django.urls import path
from api.views import PostApiView, PostDetailView, PostDeleteView, PostUpdateView, PostCreateView

urlpatterns = [
    path('posts/', PostApiView.as_view(), name='post'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete')



]