# secure_iot_framework

This project provides a secure framework for Internet of Things (IoT) devices, focusing on authentication, encryption, secure communication, and device management.

## Folder Structure

- `config/`: Contains configuration files.
- `core/`: Core functionality of the framework.
- `devices/`: Sample devices.
- `web/`: Web interface for managing devices.
- `tests/`: Unit tests.
- `database/`: Directory for the SQLite database.
- `main.py`: Main entry point.
- `README.md`: Project documentation.
- `requirements.txt`: Project dependencies.

## Setup
1. Clone the repository.
2. Install the dependencies
```bash
pip install -r requirements.txt
```
3. Make sure the database directory exists
```bash
mkdir -p database
```
4. Initialize the database
```bash
python -c "from core.device_management import DeviceManager; DeviceManager()"
```
5. Start the flask server
```bash
python web/app.py
```
6. Start the application
```bash
python main.py
```
