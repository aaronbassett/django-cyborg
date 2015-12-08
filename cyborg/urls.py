# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.views.generic import TemplateView

cyborg_patterns = [
    url(
        r'^robots\.txt$',
        TemplateView.as_view(
            template_name='cyborg/robots.txt',
            content_type='text/plain'
        ),
        name='robots'
    ),
    url(
        r'^humans\.txt$',
        TemplateView.as_view(
            template_name='cyborg/humans.txt',
            content_type='text/plain'
        ),
        name='humans'
    ),
]

urlpatterns = [
    url(r'', include(cyborg_patterns, namespace='cyborg'))
]
