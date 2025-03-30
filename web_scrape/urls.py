from django.urls import path
from . import views

urlpatterns = [
    # path('live_internship/', views.fetch_internships, name='live_internship'),
    # path("open-chrome/", views.open_chrome_view, name="live_internship"),
    
    path('internship/', views.internship_view, name='live_internship'),
    path('download_csv/<str:filename>/', views.download_csv, name='download_csv'),
    # Add other paths here as necessary
]
