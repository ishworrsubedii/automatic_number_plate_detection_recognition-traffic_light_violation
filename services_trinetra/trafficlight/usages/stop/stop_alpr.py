"""
Created By: ishwor subedi
Date: 2024-02-28
"""

class StopAlprExample:
    def __init__(self, stop_flag_path):
        self.stop_flag_path = stop_flag_path

    def stop_anpr_service(self):
        try:
            with open(self.stop_flag_path, 'w') as f:
                f.write('True')
            print('ANPR service stopped successfully')
        except Exception as e:
            print(f"Error updating stop flag: {e}")


if __name__ == "__main__":
    STOP_FLAG_PATH = "services_trinetra/trafficlight/resources/flag_check/alpr_status"
    stop_service = StopAlprExample(STOP_FLAG_PATH)
    stop_service.stop_anpr_service()
