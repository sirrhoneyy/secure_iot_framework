from core.authentication import Authenticator
from core.device_management import DeviceManager


class RegistrationManager:
    def __init__(self, secret_key):
        self.authenticator = Authenticator(secret_key)
        self.device_manager = DeviceManager()

    def register_device(self, device_id, device_info):
        token = self.authenticator.generate_token(device_id)
        self.device_manager.add_device(device_id, device_info)
        return token
