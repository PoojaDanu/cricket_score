from confluent_kafka import Producer

ssl_config = {
    "ca_location": "../kafka_files/ca.pem",
    "cert_location": "../kafka_files/service.cert",
    "key_location": "../kafka_files/service.key",
}

class KafkaProducer:
    def __init__(self):
        self.producer = Producer({
            'bootstrap.servers': "kafka-1ddd1fb7-adityacha703-e344.a.aivencloud.com:18505",
            'security.protocol': 'ssl',
            'ssl.ca.location': ssl_config['ca_location'],
            'ssl.certificate.location': ssl_config['cert_location'],
            'ssl.key.location': ssl_config['key_location']
        })

    def produce_message(self, topic, message):
        self.producer.produce(topic=topic, value=message)
        self.producer.flush()

    def close(self):
        self.producer.flush()
        self.producer.close()

