"""
Singleton data store

Created on 4th Dec, 2020
@author manik
"""
import tkinter as tk

class DataStore:
    __instance__ = None

    def __init__(self):
       """ Constructor.
       """
       self.population_val                      = tk.StringVar()
       self.population_val.set('1000')
       self.social_distancing_val               = tk.StringVar()
       self.social_distancing_val.set('50%')
       self.hospital_capacity_val               = tk.StringVar()
       self.hospital_capacity_val.set('20%')
       self.recovery_time_val                   = tk.StringVar()
       self.recovery_time_val.set('120')
       self.r_val                               = tk.StringVar()
       self.r_val.set('3.00')
       self.k_val                               = tk.StringVar()
       self.k_val.set("0.10")
       self.social_distancing_starting_at_val   = tk.StringVar()
       self.social_distancing_starting_at_val.set("200")
       self.mask_mandate_starting_at_val        = tk.StringVar()
       self.mask_mandate_starting_at_val.set("320")
       self.mask_effectiveness_cloth_mask       = tk.StringVar()
       self.mask_effectiveness_cloth_mask.set('50%')
       self.mask_effectiveness_surgical_mask    = tk.StringVar()
       self.mask_effectiveness_surgical_mask.set('70%')
       self.mask_effectiveness_n95_mask         = tk.StringVar()
       self.mask_effectiveness_n95_mask.set('90%')
       self.mortality_rate_zero_to_nineteen     = tk.StringVar()
       self.mortality_rate_zero_to_nineteen.set('0.03%')
       self.mortality_rate_twenty_to_fortynine  = tk.StringVar()
       self.mortality_rate_twenty_to_fortynine.set('0.02%')
       self.mortality_rate_fifty_to_sixtynine   = tk.StringVar()
       self.mortality_rate_fifty_to_sixtynine.set('0.5%')
       self.mortality_rate_seventyplus          = tk.StringVar()
       self.mortality_rate_seventyplus.set('5.4%')
       self.infection_range                     = tk.StringVar()
       self.infection_range.set('0.001')
       
       self.recovery_time_scale = None
       self.r_value_scale = None
       self.k_value_scale = None
       
       if DataStore.__instance__ is None:
           DataStore.__instance__ = self
       else:
           raise Exception("You cannot create another SingletonGovt class")

    @staticmethod
    def get_instance():
       """
       Static method to fetch the current instance
       """
       if not DataStore.__instance__:
           DataStore()
       return DataStore.__instance__

    def get_infection_range_val(self):
        return float(self.infection_range.get())

    def get_population_val(self):        
        return int(self.population_val.get())

    def get_social_distancing_val(self):
        return int(self.social_distancing_val.get().split('%')[0])

    def get_hospital_capacity_val(self):
        return int(self.hospital_capacity_val.get().split('%')[0])

    def get_recovery_time_val(self):
        return int(self.recovery_time_val.get())

    def get_social_distancing_starting_at_val(self):
        return int(self.social_distancing_starting_at_val.get())

    def get_mask_mandate_starting_at_val(self):
        return int(self.mask_mandate_starting_at_val.get())

    def get_r_val(self):
        return float(self.r_val.get())

    def get_k_val(self):
        return float(self.k_val.get())

    def get_mask_effectiveness_cloth_mask(self):
        return int(self.mask_effectiveness_cloth_mask.get().split('%')[0])

    def get_mask_effectiveness_surgical_mask(self):
        return int(self.mask_effectiveness_surgical_mask.get().split('%')[0])

    def get_mask_effectiveness_n95_mask(self):
        return int(self.mask_effectiveness_n95_mask.get().split('%')[0])

    def get_all_mask_effectiveness(self):
        self.mask_effectiveness = dict()
        self.mask_effectiveness['no_mask'] = 0
        self.mask_effectiveness['cloth_mask'] = self.get_mask_effectiveness_cloth_mask()
        self.mask_effectiveness['surgery_mask'] = self.get_mask_effectiveness_surgical_mask()
        self.mask_effectiveness['n95_mask'] = self.get_mask_effectiveness_n95_mask()
        return self.mask_effectiveness

    def get_mortality_rate_zero_to_nineteen(self):
        return float(self.mortality_rate_zero_to_nineteen.get().split('%')[0])

    def get_mortality_rate_twenty_to_fortynine(self):
        return float(self.mortality_rate_twenty_to_fortynine.get().split('%')[0])

    def get_mortality_rate_fifty_to_sixtynine(self):
        return float(self.mortality_rate_fifty_to_sixtynine.get().split('%')[0])

    def get_mortality_rate_seventyplus(self):
        return float(self.mortality_rate_seventyplus.get().split('%')[0])

    def get_all_mortality_rates(self):
        self.mortality_rate = dict()
        self.mortality_rate['0-19'] = self.get_mortality_rate_zero_to_nineteen()/100
        self.mortality_rate['20-49'] = self.get_mortality_rate_twenty_to_fortynine()/100
        self.mortality_rate['50-69'] = self.get_mortality_rate_fifty_to_sixtynine()/100
        self.mortality_rate['70-100'] = self.get_mortality_rate_seventyplus()/100
        return self.mortality_rate


    

    
