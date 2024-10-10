from django.urls import path

from measurement.views import SensorListCreateView, SensorRetrieveUpdateView, MeasurementCreateView, SensorDetailView

urlpatterns = [
    path('sensors/', SensorListCreateView.as_view()),
    path('sensors/<int:pk>/', SensorRetrieveUpdateView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
    path('sensors/<int:pk>/detail/', SensorDetailView.as_view()),
]
