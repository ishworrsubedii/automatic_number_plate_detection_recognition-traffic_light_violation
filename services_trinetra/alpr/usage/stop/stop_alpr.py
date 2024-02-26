"""
Created By: ishwor subedi
Date: 2024-02-07
"""

from services.alpr.usage import alpr_logger

ALPR_LOGGER = alpr_logger()


class StopAlprExample:
    def __init__(self, stop_flag_path):
        self.stop_flag_path = stop_flag_path

    def stop_anpr_service(self):
        try:
            with open(self.stop_flag_path, 'w') as f:
                f.write('True')
            ALPR_LOGGER.info('ANPR service stopped successfully')
        except Exception as e:
            ALPR_LOGGER.error(f"Error updating stop flag: {e}")


if __name__ == "__main__":
    STOP_FLAG_PATH = "services/alpr/resources/flag_check/alpr_status.txt"
    stop_service = StopAlprExample(STOP_FLAG_PATH)
    stop_service.stop_anpr_service()
