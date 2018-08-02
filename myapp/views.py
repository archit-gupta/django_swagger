# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from serializers import ComputerSerializer
from models import Computer
# Create your views here.


def permission_denied_handler(request):
    from django.http import HttpResponse
    return HttpResponse('you have no permissions!')

class ComputerViewSet(viewsets.ModelViewSet):

    serializer_class = ComputerSerializer
    def get_queryset(self):
        """ Get all Computer object """
        return super(ComputerViewSet, self).all()

    def create(self, request):
        """ creates a Computer object """
        return super(ComputerViewSet, self).create(request)
    
    def retrieve(self, request, pk=None):
        """Returns a single Computer item"""
        return super(ComputerViewSet, self).retrieve(request, pk)

    def update(self, request, *args, **kwargs):
        """Updates a single Computer item"""
        return super(ComputerViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """Partial update a Computer """
        return super(ComputerViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, pk=None):
        """Delete a Computer"""
        return super(ComputerViewSet, self).destroy(request, pk)
