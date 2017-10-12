import datetime

from django.db import models
from django.contrib.auth.models import User

from django.contrib import admin

class MicroPost(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    display = models.BooleanField('display post')

    def __unicode__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= datetime.datetime.today() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Tag(models.Model):
    microPost = models.ForeignKey(MicroPost)
    tag = models.CharField(max_length=30)

    def __unicode__(self):
        return self.tag

class TagInLine(admin.TabularInline):
    model = Tag

class MicroPostAdmin(admin.ModelAdmin):
    inlines = [TagInLine]
    list_display = ('title','pub_date','user','was_published_recently')
    list_filter = ['pub_date','display']


admin.site.register(MicroPost,MicroPostAdmin)
admin.site.register(Tag)