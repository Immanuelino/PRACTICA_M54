# myapp/urls.py

from django.urls import path
from .views import ProtectedListView, home  # Asegúrate de que la importación sea correcta

urlpatterns = [
    path('', home, name='home'),  # Ruta de inicio
    path('my-products/', ProtectedListView.as_view(), name='my-products'),
]
