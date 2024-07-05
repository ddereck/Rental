from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes

# start_cron()

@api_view(['GET'])
@permission_classes([AllowAny])
def home(request):
    return Response({
        'message': 'Welcome to the CARS-SERVICE.',
        'version': '1.0.0',
        'authors': 'Gilles-Déreck GNANCADJA',
        'address': 'itgillo60@gmail.com',
        'example': {
            'notice': '_______________________________________',
            'url': request.build_absolute_uri() + '____________'
        }
    }, status=201)
