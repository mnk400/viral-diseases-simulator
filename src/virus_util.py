from config_util import ConfigUtil
from person import Person

class Virus():
    """
    This class provides abstraction to all virus related properties and methods such as 
    infecting, healing and dying
    """    

    def __init__(self):
        """
        The constructor is responsible for loading the virus statistics from the config file
        """  
        config = ConfigUtil("config/config.ini")
        self.infection_range        = config.getFloatValue("virus.stats", "infection_range")
        self.k_value                = config.getFloatValue("virus.stats", "k_value")
        self.reproduction_rate      = config.getFloatValue("virus.stats", "reproduction_rate")
        self.mortality_rate         = config.getFloatValue("virus.stats", "mortality_rate")
        self.mask_effectiveness     = config.getFloatValue("virus.stats", "mask_effectiveness")
        self.recovery_time          = config.getFloatValue("virus.stats", "recovery_time")

    def infect(self, persons: Person):

        #Get the index of all the people who were infected in the previous step
        infected_idx = persons.get_all_infected()

        healthy_atrisk = []        
        #Get the index of all the people within the infection range of the infected persons


