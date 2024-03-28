from aiokafka import AIOKafkaProducer

class MessageProducer:
    __message_producer:AIOKafkaProducer = None

    def setup_producer(self) -> AIOKafkaProducer:
        kafka_producer = AIOKafkaProducer(bootstrap_servers="kafka-1ddd1fb7-adityacha703-e344.a.aivencloud.com:18505")
        MessageProducer.__message_producer = kafka_producer
        return self.__message_producer;

    def send(self, message , topic):
        self.__kafka_producer.send(topic ,message)