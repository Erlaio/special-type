from django.contrib import admin
from api.models import Feedback, Schedule, Playbill
from api.models import News, People, Companies, NewsImage


class NewsImageAdmin(admin.StackedInline):
    model = NewsImage


class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsImageAdmin]


admin.site.register(Feedback)
admin.site.register(Schedule)
admin.site.register(Playbill)
admin.site.register(News, NewsAdmin)
admin.site.register(People)
admin.site.register(Companies)
