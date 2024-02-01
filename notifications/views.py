from rest_framework import viewsets
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer
from confluent_kafka import Producer
from django.conf import settings

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        self.publish_to_kafka(serializer.data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)
    
    def perform_create(self, serializer):
        serializer.save()

    def publish_to_kafka(self, data):
        try:
            producer_conf = {
              'bootstrap.servers': settings.KAFKA_SERVER,
              'security.protocol': 'SASL_SSL',
              'sasl.mechanisms': 'PLAIN',
              'sasl.username': settings.KAFKA_API_KEY,
              'sasl.password': settings.KAFKA_API_SECRET
            }

            producer = Producer(producer_conf)
            producer.produce(settings.KAFKA_TOPIC, value=str(data))
            producer.flush()
        except Exception as e:
            print(f"Error publishing to Kafka: {str(e)}")