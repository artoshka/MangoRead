from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework.generics import ListAPIView
from rest_framework import views
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter

from .service import MangaFilter
from .permission import IsAuthenticationOrReadOnly
from .models import Manga, Review
from .serializers import MangoSerializer, ReviewSerializer, ReviewCreateSerializer, MangoDetailSerializer


class MangaPagination(PageNumberPagination):
    page_size = 12
    page_query_param = "page_size"
    max_page_size = 100


class MangaAPIView(ListAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangoSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, )
    search_fields = ("name", )
    filterset_class = MangaFilter
    pagination_class = MangaPagination


class MangaDetailAPIView(views.APIView):
    permission_classes = (IsAuthenticationOrReadOnly, )

    def get(self, request, id):
        try:
            queryset = Manga.objects.get(id=id)
        except:
            return Response(data={"errors": "Manga not found"}, status=404)
        review = Review.objects.all().filter(manga_id__id=id)
        paginator = PageNumberPagination()
        paginator.page_size = 3
        result_page = paginator.paginate_queryset(review, request)
        serializer = ReviewSerializer(result_page, many=True)
        serializer_s = MangoDetailSerializer(queryset)
        return paginator.get_paginated_response({"manga": serializer_s.data,
                                                 "reviews": serializer.data})

    def post(self, request, id):
        serializer = ReviewCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)

        return Response({"post": serializer.data}, status=201)


