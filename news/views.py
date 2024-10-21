from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import News
from .serializers import NewsSerializer
from account.permissions import IsAuthenticatedOrReadOnly

# Create your views here.


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

@api_view(['GET', 'POST'])
def news_list(request):
    if request.method == 'GET':
        # GET 요청일 경우에는 모든 사용자가 접근 가능하도록 함
        projects = News.objects.all()
        serializer = NewsSerializer(projects, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # POST 요청일 경우에만 인증 요구
        if not request.user.is_authenticated:
            return Response({'detail': 'Authentication required.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def project_detail(request, pk):
    try:
        project = News.objects.get(pk=pk)
    except News.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NewsSerializer(project)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = NewsSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)