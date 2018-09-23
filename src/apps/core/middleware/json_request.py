from django.utils.deprecation import MiddlewareMixin


class JsonParseRequest(MiddlewareMixin):

    def process_request(self, request):
        request.AXIOS = dict()
        if request.META['CONTENT_TYPE'] == 'application/json':
            import json
            request.AXIOS = json.loads(request.body.decode('utf-8'))

