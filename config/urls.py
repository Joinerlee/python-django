from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from news.views import NewsViewSet
from members.views import MemberViewSet
from researches.views import ResearchViewSet
from gallery.views import GalleryViewSet
from projects.views import ProjectViewSet  # ProjectViewSet을 import 합니다
from publications.views import PublicationViewSet  # PublicationViewSet을 import 합니다


router = DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'members', MemberViewSet)
router.register(r'researches', ResearchViewSet)
router.register(r'gallery', GalleryViewSet)
router.register(r'projects', ProjectViewSet)  # ProjectViewSet을 router에 등록합니다
router.register(r'publications', PublicationViewSet)  # PublicationViewSet을 router에 등록합니다

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('projects/', include('projects.urls')),
    path('account/', include('account.urls')),  # 이 부분은 올바르게 설정되어 있습니다
    path('researches/', include('researches.urls')),  # HTML 템플릿 렌더링을 위한 경로
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)