# coding: UTF-8

from tastypie.resources import ModelResource
from tastypie.authentication import Authentication, BasicAuthentication
from tastypie.authorization import Authorization

from models import *

class DjangoAuthentication(Authentication):
    def is_authenticated(self, request, **kwargs):
        if getattr(request, 'user', False) and request.user.is_authenticated():
            return True
        return False 

    def get_identifier(self, request):
        return request.user.username


class OperationResource(ModelResource):
    class Meta:
        list_allowed_methods = ['get', 'post', 'put']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'operation'
        queryset = Operation.objects.all()
        authentication = DjangoAuthentication()
        authorization = Authorization()
