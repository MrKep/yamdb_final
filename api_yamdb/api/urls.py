from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet)

app_name = 'api'

router = DefaultRouter()

router.register('categories', CategoryViewSet, basename='categorys')
router.register('genres', GenreViewSet, basename='genres')
router.register('titles', TitleViewSet, basename='titles')
router.register(r'titles/(?P<title_id>[\d]+)/reviews',
                ReviewViewSet, basename='reviews')
router.register(r'titles/(?P<title_id>[\d]+)'
                r'/reviews/(?P<review_id>[\d]+)/comments', CommentViewSet,
                basename='comments')


urlpatterns = [
    path('api/v1/', include(router.urls)),
]
