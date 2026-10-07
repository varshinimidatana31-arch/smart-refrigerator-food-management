import random
from datetime import datetime

class SmartFridgeTelemetry:
    def __init__(self):
        self.target_temp = 4.0 # Celsius
        self.target_humidity = 65 # %
        self.door_open = False
        self.camera_status = "Active / HD Stream Ready"
        self.wifi_status = "Connected (5G Cloud Sync)"

    def get_telemetry(self):
        # Add slight natural fluctuation
        temp_var = random.uniform(-0.3, 0.4)
        hum_var = random.randint(-2, 2)
        
        current_temp = round(self.target_temp + temp_var, 1)
        current_hum = max(40, min(90, self.target_humidity + hum_var))
        
        temp_status = "Optimal" if 2.0 <= current_temp <= 6.0 else "Warning: Check Thermostat"
        
        return {
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "temperature_c": current_temp,
            "temperature_status": temp_status,
            "humidity_pct": current_hum,
            "humidity_status": "Optimal Freshness Level",
            "door_state": "CLOSED" if not self.door_open else "OPEN (Alert)",
            "camera_sensor": self.camera_status,
            "cloud_sync": self.wifi_status,
            "rpi_cpu_usage": f"{random.randint(12, 28)}%",
            "rpi_memory": "1.4 GB / 8.0 GB"
        }

if __name__ == "__main__":
    t = SmartFridgeTelemetry()
    print("IoT Telemetry Sample:", t.get_telemetry())
