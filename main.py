from core import Authenticator, Communicator, DeviceManager, Encryptor, Logger, RegistrationManager, Scheduler
from config.config import config
import random


def main():
    authenticator = Authenticator(config.SECRET_KEY)
    communicator = Communicator()
    device_manager = DeviceManager()
    encryptor = Encryptor(config.ENCRYPTION_KEY)
    logger = Logger()
    registration_manager = RegistrationManager(config.SECRET_KEY)

    device_id = str(random.randint(0, 5000))
    device_info = f'Device {device_id} Info'
    token = registration_manager.register_device(device_id, device_info)
    logger.log(f'{device_id} registered with token: {token}')

    if authenticator.authenticate_device(device_id, token):
        logger.log(f'{device_id} authenticated successfully')
        data = 'Hello, IoT!'
        encrypted_data = encryptor.encrypt(data)
        communicator.send_data({'device_id': device_id, 'data': encrypted_data})
        logger.log(f'Encrypted data sent from {device_id}')

    def collect_data():
        data = f'Sensor data from {device_id}'
        encrypted_data = encryptor.encrypt(data)
        communicator.send_data({'device_id': device_id, 'data': encrypted_data})
        logger.log(f'Encrypted data sent from {device_id}: {data}')

    scheduler = Scheduler(5, collect_data)
    scheduler.start()


if __name__ == '__main__':
    main()
