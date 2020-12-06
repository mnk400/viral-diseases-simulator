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
       self.recovery_time_val.set('150')
       self.r_val                               = tk.StringVar()
       self.r_val.set('3.00')
       self.k_val                               = tk.StringVar()
       self.k_val.set("0.10")
       self.social_distancing_starting_at_val   = tk.StringVar()
       self.social_distancing_starting_at_val.set("200")
       self.mask_mandate_starting_at_val        = tk.StringVar()
       self.mask_mandate_starting_at_val.set("200")

       if DataStore.__instance__ is None:
           DataStore.__instance__ = self
       else:
           raise Exception("You cannot create another SingletonGovt class")

   @staticmethod
   def get_instance():
       """ Static method to fetch the current instance.
       """
       if not DataStore.__instance__:
           DataStore()
       return DataStore.__instance__