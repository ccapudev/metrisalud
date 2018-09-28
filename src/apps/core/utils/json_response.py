# -*- coding: utf-8 -*-
import json
from decimal import Decimal
from django.http import JsonResponse as JsonResponseNative
from django.db.models import Model
from django.forms.models import model_to_dict


def parse_objects(obj):
    print(obj)
    import datetime
    if isinstance(obj, datetime.datetime):
        return obj.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
    if isinstance(obj, datetime.date):
        return obj.strftime('%Y-%m-%d')
    if isinstance(obj, Model):
        return model_to_dict(obj)
    if isinstance(obj, Decimal):
        return str(obj)
    if isinstance(obj, list):
        return iter(obj)


class JsonResponseMixin(JsonResponseNative):
    '''
        Modelo render para tipos de datos comunes
    '''
    def __init__(self, *args, **kwargs):
        kwargs['json_dumps_params'] = dict(
            default=parse_objects,
        )
        super().__init__(*args, **kwargs)


__all__ = [
    'JsonResponseMixin'
]
