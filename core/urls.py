from django.contrib import admin
from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.response import Response
import importlib

@api_view(['GET'])
def health(request):
    dependencies = {
        'keras': False, 
        'numpy': False, 
        'PIL': False, 
        'sklearn': False,
        'tensorflow': False
    }
    
    status = 'healthy'
    code = 200
    for lib in dependencies.keys(): 
        try:
            importlib.import_module(lib)
            dependencies[lib] = True
        except ImportError: 
            status = 'unhealthy'
            code = 500
            pass
    
    return Response({
        'status': status, 
        'dependencies': dependencies
    }, status = code)

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api/v1/', include('mnist_app.urls')), 
    path('health/', health, name = 'health')
]