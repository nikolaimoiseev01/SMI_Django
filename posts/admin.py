import re

from django.contrib import admin
from django.utils.html import strip_tags, format_html

from .models import *
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget


@admin.register(Post)
class CustomAdminClass(ModelAdmin):
    # pass

    list_display = ['id', 'title', 'Обложка', 'Текст']
    list_display_links = ['id', 'title', 'Обложка', 'Текст']

    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }

    # #
    def Обложка(self, obj):
        return format_html(f'<img src="/media/{obj.cover_img}" style="width:200px; object-fit: cover; height:100px"/>')

    def Текст(self, obj):
        def textify(html):
            # Remove html tags and continuous whitespaces
            text_only = re.sub('[ \t]+', ' ', strip_tags(html))
            # Strip single spaces in the beginning of each line
            return text_only.replace('\n ', '\n').strip()

        return textify(obj.text)[0:150]


@admin.register(PostTopic)
class CustomAdminClass(ModelAdmin):
    list_display = ['id', 'name']
