from rest_captcha.serializers import RestCaptchaSerializer
from rest_framework.serializers import ModelSerializer

from .models import Feedback, Schedule, Playbill, News
from .models import Companies, NewsImage, People


class FeedbackModelSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'date', 'description', 'name', 'images']


class ScheduleModelSerializer(ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'name', 'address', 'date']


class PlaybillModelSerializer(ModelSerializer):
    class Meta:
        model = Playbill
        fields = ['id', 'name', 'address', 'date', 'price']


class NewsImageModelSerializer(ModelSerializer):
    class Meta:
        model = NewsImage
        fields = ['image', 'news']


class NewsModelSerializer(ModelSerializer):
    images = NewsImageModelSerializer(
        many=True
    )

    class Meta:
        model = News
        fields = ['id', 'date', 'name', 'description', 'images',
                  'video']



class PeopleModelSerializer(ModelSerializer):
    class Meta:
        model = People
        fields = ['id', 'images', 'first_name', 'last_name', 'description']


class CompaniesModelSerializer(ModelSerializer):
    class Meta:
        model = Companies
        fields = ['id', 'images', 'name', 'description']
