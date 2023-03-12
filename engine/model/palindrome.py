from datetime import datetime

from engine.sternman_engine import SternmanEngine


class Palindrome(SternmanEngine):
    def needs_service(self):
        # Calculate the service threshold date as four years after the last service date
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        
        # Check if the service threshold date has passed or if the engine should be serviced due to a warning light
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
