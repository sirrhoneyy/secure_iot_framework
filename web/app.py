from flask import Flask, request, redirect, url_for
from core.device_management import DeviceManager
from core.registration import RegistrationManager
from config.config import config
from core.encryption import Encryptor

app = Flask(__name__)
device_manager = DeviceManager()
registration_manager = RegistrationManager(config.SECRET_KEY)
encryptor = Encryptor(config.ENCRYPTION_KEY)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    print(f'Received data: {data}')
    device_data = data.get('data')
    decrypted_device_data = encryptor.decrypt(device_data)
    print(f'Decrypted data: {decrypted_device_data}')
    return 'Data received', 200


if __name__ == '__main__':
    app.run(host='localhost', port=8000)
