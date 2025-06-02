from django.urls import path
from . import views

urlpatterns = [
    path('', views.CircuitIDListView.as_view(), name='circuitid_list'),
    path('<int:pk>/', views.CircuitIDDetailView.as_view(), name='circuitid_detail'),
]
