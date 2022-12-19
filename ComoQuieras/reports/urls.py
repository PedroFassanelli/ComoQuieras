from django.urls import path
from reports.views import ReportePersonalizadoExcel

urlpatterns = [
    path('reporte/',ReportePersonalizadoExcel.as_view(), name = 'reporte'),

]