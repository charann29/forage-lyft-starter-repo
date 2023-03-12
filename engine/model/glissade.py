from datetime import datetime
from engine.willoughby_engine import WilloughbyEngine

class Glissade(WilloughbyEngine):
    def needs_service(self):
        # Calculate the date that the engine needs to be serviced by adding 2 years to the last service date
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        
        # Check if the calculated service threshold date has already passed or if the engine should be serviced based on mileage
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
