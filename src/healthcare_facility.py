from config_util import ConfigUtil

class HealthcareFacility(object):

    def __init__(self) -> None:
        self.config = ConfigUtil('config/config.ini')
        self.total_healthcare_capacity = self.config.getIntegerValue("area", "healthcare_capacity_ratio")*(self.config.getIntegerValue("area", "healthcare_capacity_ratio")/100)
        self.current_capacity = self.total_healthcare_capacity

    def admit_patient(self):
        self.current_capacity -= 1

    def check_capacity_full(self):
        return self.current_capacity == 0