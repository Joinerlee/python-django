from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Gallery
from .serializers import GallerySerializer
from account.permissions import IsAuthenticatedOrReadOnly


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


@api_view(['GET', 'POST'])
def gallery_list(request):
    if request.method == 'GET':
        # GET 요청일 경우에는 모든 사용자가 접근 가능하도록 함
        projects = Gallery.objects.all()
        serializer = GallerySerializer(projects, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # POST 요청일 경우에만 인증 요구
        if not request.user.is_authenticated:
            return Response({'detail': 'Authentication required.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = GallerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)