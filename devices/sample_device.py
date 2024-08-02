from core import Communicator, Encryptor, Logger
from config.config import config


class SampleDevice:
    def __init__(self, device_id):
        self.device_id = device_id
        self.communicator = Communicator()
        self.encryptor = Encryptor(config.ENCRYPTION_KEY)
        self.logger = Logger()

    def send_data(self, data):
        encrypted_data = self.encryptor.encrypt(data)
        self.communicator.send_data({'device_id': self.device_id, 'data': encrypted_data})
        self.logger.log(f'Data sent from {self.device_id}: {data}')

    # def receive_data(self):
    #     data = self.communicator.receive_data()
    #     decrypted_data = self.encryptor.decrypt(data['data'])
    #     self.logger.log(f'Data received by {self.device_id}: {decrypted_data}')
    #     return decrypted_data
