#!/usr/bin/env python
#-*- coding: utf-8 -*-
from django.db import models


class Team(models.Model):
        name = models.CharField(max_length = 150)
        description = models.TextField()
        logo = models.ImageField()
        code = models.CharField(max_length = 100)
        
        def __str__(self):
                return self.code

        def image_tag(self):
                return u'<img src="%s"/>'%(logo)
        image_tag.short_description = 'logo'
        image_tag.allow_tags = True
class Player(models.Model):
        name = models.CharField(max_length = 150)
        alias = models.CharField(max_length = 100)
        birthday = models.DateField()
        age = models.IntegerField()
        rut = models.CharField(max_length = 30)
        email = models.CharField(max_length = 100)
        height = models.FloatField()
        weight = models.FloatField()
        image = models.ImageField()
        position = models.CharField(max_length = 100)
        team = models.ForeignKey(Team, on_delete = models.CASCADE,default = None)

        def __str__(self):
                return self.rut

class Coach(models.Model):
        name = models.CharField(max_length = 150)
        age = models.IntegerField()
        email = models.CharField(max_length = 100)
        rut = models.CharField(max_length = 30)
        alias = models.CharField(max_length = 100)


        def __str__(self):
                return self.rut

class Model_match(models.Model):
        name = models.CharField(max_length = 150)
        def __str__(self):
                return self.name
                
                
                
        
                


