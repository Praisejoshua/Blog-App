from django.urls import path
from .views import HomeView, BlogCreate, BlogDetailView, UpdateDetailsView, DeleteDetailsView, ProfileHomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/new/', BlogCreate.as_view(), name='new_post'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', UpdateDetailsView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', DeleteDetailsView.as_view(), name='post_delete'),
    path('profile/', ProfileHomeView.as_view(), name= 'profile')

]
