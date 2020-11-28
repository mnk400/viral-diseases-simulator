from config_util import ConfigUtil
from person import Person

class Virus():

    def __init__(self):
        """
        [summary]
        """  
        config = ConfigUtil("config/config.ini")
        self.infection_range        = config.getFloatValue("virus.stats", "infection_range")
        self.k_value                = config.getFloatValue("virus.stats", "k_value")
        self.reproduction_rate      = config.getFloatValue("virus.stats", "reproduction_rate")
        self.mortality_rate         = config.getFloatValue("virus.stats", "mortality_rate")
        self.mask_effectiveness     = config.getFloatValue("virus.stats", "mask_effectiveness")
        self.recovery_time          = config.getFloatValue("virus.stats", "recovery_time")

    def infect(self, persons: Person):

        infected_idx = persons.get_dataframe().index[persons.get_dataframe()['current_state'] == 1].tolist()

