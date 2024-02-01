from confluent_kafka import Consumer
from firebase_admin import initialize_app, messaging
from django.conf import settings
import os
from django import setup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'push_notification_api.settings')
setup()
def kafka_consumer():
    consumer_conf = {
        'bootstrap.servers': settings.KAFKA_SERVER,
        'group.id': 'my_group',
        'security.protocol': 'SASL_SSL',
        'sasl.mechanisms': 'PLAIN',
        'sasl.username': settings.KAFKA_API_KEY,
        'sasl.password': settings.KAFKA_API_SECRET,
    }
    consumer = Consumer(consumer_conf)
    consumer.subscribe([settings.KAFKA_TOPIC])

    initialize_app()

    while True:
        msg = consumer.poll(1.0)
        print(f"{msg}")
        print(f"Within While")
        if msg is None:
            print("No message received")
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue
        try:
            print(f"Received message: {msg.value()}")
            print(f"Message details: {msg}")
            data = eval(msg.value())
            print(f"Message topic: {data['message']}")
            send_push_notification(data['message'])
        except Exception as e:
            print(f"Error processing message: {str(e)}")

def send_push_notification(message):
    # Use Firebase Cloud Messaging to send push notification
    message = messaging.Message(
        data={'message': message},
        token='device_token_here'  # Replace with the actual device token
    )
    response = messaging.send(message)
    print(f"Notification sent: {response}")

if __name__ == '__main__':
    kafka_consumer()