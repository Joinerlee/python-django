from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Research
from .serializers import ResearchSerializer



class ResearchViewSet(viewsets.ModelViewSet):
    queryset = Research.objects.all()
    serializer_class = ResearchSerializer


@api_view(['GET', 'POST'])
def research_list(request):
    if request.method == 'GET':
        # GET 요청일 경우에는 모든 사용자가 접근 가능하도록 함
        researches = Research.objects.all()
        serializer = ResearchSerializer(researches, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # POST 요청일 경우에만 인증 요구
        if not request.user.is_authenticated:
            return Response({'detail': 'Authentication required.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = ResearchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def research_detail(request, pk):
    try:
        research = Research.objects.get(pk=pk)
    except Research.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ResearchSerializer(research)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ResearchSerializer(research, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        research.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)