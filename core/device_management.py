import sqlite3
import os
from config.config import config


class DeviceManager:
    def __init__(self):
        os.makedirs(os.path.dirname(config.DATABASE_URI), exist_ok=True)
        self.conn = sqlite3.connect(config.DATABASE_URI)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS devices (
                    id TEXT PRIMARY KEY,
                    info TEXT
                )
            """)

    def add_device(self, device_id, device_info):
        with self.conn:
            self.conn.execute("INSERT INTO devices (id, info) VALUES (?, ?)", (device_id, device_info))

    def remove_device(self, device_id):
        with self.conn:
            self.conn.execute("DELETE FROM devices WHERE id = ?", (device_id,))

    def get_device(self, device_id):
        cursor = self.conn.execute("SELECT info FROM devices WHERE id = ?", (device_id,))
        row = cursor.fetchone()
        return row[0] if row else None

    def list_devices(self):
        cursor = self.conn.execute("SELECT id, info FROM devices")
        return cursor.fetchall()
