from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Feedback, Schedule, Playbill, News, \
    People, Companies
from .pagination import ApiPagination
from .serializers import FeedbackModelSerializer, \
    ScheduleModelSerializer, \
    PlaybillModelSerializer, NewsModelSerializer, PeopleModelSerializer, \
    CompaniesModelSerializer, RestCaptchaSerializer
from rest_framework import filters, mixins, viewsets, views
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


class CaptureCheckViewSet(views.APIView):
    def post(self, request):
        serializer = RestCaptchaSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"ok":'Check'})
        raise ValidationError(detail='validation error')


class FeedbackModelViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin,
                           viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackModelSerializer
    pagination_class = ApiPagination


class ScheduleModelViewSet(ReadOnlyModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleModelSerializer
    pagination_class = ApiPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class PlaybillModelViewSet(ReadOnlyModelViewSet):
    queryset = Playbill.objects.all()
    serializer_class = PlaybillModelSerializer
    pagination_class = ApiPagination


class NewsModelViewSet(ReadOnlyModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsModelSerializer
    pagination_class = ApiPagination


class PeopleModelViewSet(ReadOnlyModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleModelSerializer
    pagination_class = ApiPagination


class CompanyModelViewSet(ReadOnlyModelViewSet):
    queryset = Companies.objects.all()
    serializer_class = CompaniesModelSerializer
    pagination_class = ApiPagination
