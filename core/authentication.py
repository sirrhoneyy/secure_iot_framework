import hashlib


class Authenticator:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def authenticate_device(self, device_id, token):
        expected_token = hashlib.sha256(f"{device_id}{self.secret_key}".encode()).hexdigest()
        return token == expected_token

    def generate_token(self, device_id):
        return hashlib.sha256(f"{device_id}{self.secret_key}".encode()).hexdigest()
