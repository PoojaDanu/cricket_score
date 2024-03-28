from django.http import HttpResponse
from .kafka_producer import KafkaProducer

async def homepage(request):
    __kafka_produce = KafkaProducer()
    __kafka_produce.produce_message("score","himanshu")
    return HttpResponse('homepage')