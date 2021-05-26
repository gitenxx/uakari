from rest_framework.decorators import api_view
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .redis import get_keys, get_specific_key, get_expiration_time, delete_one_url, delete_all_urls
from .models import Record
from .serializers import RecordSerializer, OneUrlSerializer
from .file_processing import URLProcessor


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


@api_view(['GET'])
def get_urls(request):
    return JsonResponse(get_keys(), safe=False)

@api_view(['GET'])
def get_specific_url(request):
    spkey = request.data['spkey']
    return JsonResponse({'short_url': spkey,
                        'long_url': get_specific_key(request.data['spkey']),
                        'expiration time': get_expiration_time(spkey)
                        })


@api_view(['POST'])
@csrf_exempt
def process_url(request):
    serializer = OneUrlSerializer(data=request.data)
    if serializer.is_valid():
        processor = URLProcessor()
        url = processor.process_url(long_url=serializer.validated_data['long_url'],
                                    expiration_time=serializer.validated_data['expiration_time'],
                                    max_hash_length=serializer.validated_data['max_hash_length'])
        return JsonResponse({"short_url": url,
                            "expiration_time": request.data['expiration_time']})
    return JsonResponse({"serializer_is_invalid": request.data})


@api_view(['DELETE'])
def delete_url(request):
    return JsonResponse({"deleted_key": delete_one_url(request.data['key'])})


@api_view(['DELETE'])
def delete_all(request):
    if int(request.data['delete']) == 1:
        delete_all_urls()
        return JsonResponse({"bd_cleared": 1})
    return JsonResponse({"bd_cleared": 0})
