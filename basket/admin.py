#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from basket.models import Team, Player, Coach, Model_match
from django.utils.safestring import mark_safe

@admin.register(Team)
class Team(admin.ModelAdmin):
        # list_fields = ('name','logo',)
        search_fields = ['name']

        list_display = ['name','code','get_thumbnail']
        def get_thumbnail(self, obj):
              return mark_safe("<img src='%s' width = '40' height = '40' >" % obj.logo.url)
        get_thumbnail.allow_tags = True
        get_thumbnail.__name__ = 'logo'
        # list_display = ['name']
        # list_filter = ['name']
        
@admin.register(Player)
class Player(admin.ModelAdmin):

        search_fields = ['name','alias','rut']
        list_filtert = ['team','birthday']

        list_display = ['name','rut','get_thumbnail']
        def get_thumbnail(self, obj):
              return mark_safe("<img src='%s' width = '40' height = '40' >" % obj.image.url)
        get_thumbnail.allow_tags = True
        get_thumbnail.__name__ = 'image'


@admin.register(Coach)
class Coach(admin.ModelAdmin):
        list_display = ['name']

@admin.register(Model_match)
class Model_match(admin.ModelAdmin):
        list_display = ['name']
