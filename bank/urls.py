from .views import DetailView, ListView
from django.urls import path

urlpatterns = {
    path('ifsc/<str:ifsc>/', DetailView.as_view()),
    path('branches/<str:bank_name>/<str:city>', ListView.as_view())
}