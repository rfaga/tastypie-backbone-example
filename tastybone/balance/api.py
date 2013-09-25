# coding: UTF-8

from tastypie.resources import ModelResource

from models import *

class OperationResource(ModelResource):
    class Meta:
        list_allowed_methods = ['get', 'post', 'put']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'operation'
        queryset = Operation.objects.all()
