from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine


class Rorschach(WilloughbyEngine):
    def needs_service(self):
        # Calculate the service threshold date as 4 years after the last service date
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        
        # Check if the service threshold date has passed or if the engine needs servicing according to other criteria
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
