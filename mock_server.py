from flask import Flask, request, jsonify, render_template_string
from collections import defaultdict
import time
import threading

app = Flask(__name__)

# Dictionary to store devices and their last data sent time
connected_devices = defaultdict(lambda: {"last_seen": None, "data_count": 0})

# Alert threshold in seconds (e.g., 60 seconds)
ALERT_THRESHOLD = 60

def check_inactivity():
    """Continuously checks if any connected devices have been inactive for longer than the ALERT_THRESHOLD."""
    while True:
        current_time = time.time()
        for device_id, info in list(connected_devices.items()):
            if info['last_seen']:
                last_seen_time = time.mktime(time.strptime(info['last_seen'], '%Y-%m-%d %H:%M:%S'))
                if current_time - last_seen_time > ALERT_THRESHOLD:
                    print(f"ALERT: Device {device_id} has not sent data for over {ALERT_THRESHOLD} seconds.")
        time.sleep(60)

@app.route('/')
def home():
    """Renders the home page with real-time data updates using jQuery and AJAX."""
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Taiwo IoT Framework Server</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f8ff;
                color: #333;
                text-align: center;
                margin: 0;
                padding: 0;
            }
            header {
                background-color: #4682b4;
                color: white;
                padding: 20px;
                font-size: 24px;
            }
            .content {
                margin: 20px;
            }
            table {
                width: 80%;
                margin: 20px auto;
                border-collapse: collapse;
            }
            table, th, td {
                border: 1px solid black;
            }
            th, td {
                padding: 10px;
                text-align: center;
            }
        </style>
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <script>
            $(document).ready(function(){
                function fetchDeviceData() {
                    $.ajax({
                        url: "/get_device_data",
                        type: "GET",
                        success: function(data) {
                            var tableRows = "";
                            $.each(data, function(device_id, info) {
                                tableRows += "<tr><td>" + device_id + "</td><td>" + info.last_seen + "</td><td>" + info.data_count + "</td></tr>";
                            });
                            $("table tbody").html(tableRows);
                        }
                    });
                }

                // Fetch device data every 5 seconds
                setInterval(fetchDeviceData, 5000);

                // Initial fetch
                fetchDeviceData();
            });
        </script>
    </head>
    <body>
        <header>
            Welcome to the Taiwo IoT Framework Server!
        </header>
        <div class="content">
            <p>Current Devices Connected:</p>
            <table>
                <thead>
                    <tr>
                        <th>Device ID</th>
                        <th>Last Seen</th>
                        <th>Data Sent Count</th>
                    </tr>
                </thead>
                <tbody>
                    <!-- Device data will be dynamically inserted here -->
                </tbody>
            </table>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

@app.route('/get_device_data', methods=['GET'])
def get_device_data():
    """API endpoint to return the connected devices data as JSON."""
    return jsonify(connected_devices)

@app.route('/data', methods=['POST'])
def receive_data():
    """Endpoint to receive data from devices. It updates the connected devices' information."""
    data = request.json
    device_id = data.get('device_id')
    if device_id:
        connected_devices[device_id]['last_seen'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        connected_devices[device_id]['data_count'] += 1
    print(f"Received data: {data}")
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    threading.Thread(target=check_inactivity, daemon=True).start()
    app.run(host='0.0.0.0', port=8000)

