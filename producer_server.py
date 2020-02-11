from kafka import KafkaProducer
import json
import time


class ProducerServer(KafkaProducer):

    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic

    # DONE send json data
    def generate_data(self):
        with open(self.input_file) as f:
            data = json.load(f)
            for item in data:
                message = self.dict_to_binary(item)
                # DONE send the correct data
                self.send(self.topic, message)
                time.sleep(1)

    # DONE fill this in to return the json dictionary to binary
    def dict_to_binary(self, json_dict):
        return json.dumps(json_dict).encode('utf-8')
        