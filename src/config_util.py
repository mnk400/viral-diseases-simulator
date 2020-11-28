'''
This file contains code written to easily interact with the 
configuration file.

Created on Jan 22, 2020
@author: manik
'''

import configparser
import os
import logging

# Calling and initializing a logger instance
logging.getLogger("configlog")                          

class ConfigUtil(object):
    '''
     his class is responsible for reading and parsing the configuration files.
     Apache.commons.configuration is used to parse the files.
    '''

    _instance = ()
    def getInstance():
        return ConfigUtil._instance
    
    def __init__(self, path_param):
        '''
         Constructor
         Responsible for calling the load function to load configuration data from the file.
         This constructor loads the default specified path as the config file if no other file path is input.
        '''
        self.parser = configparser.ConfigParser()
        self.filepath = path_param
        # Path to the configuration file from current Dir
        self.configLoaded = False
        self.loadConfigData()

    def getValue(self, section_str, key_str):
        '''
         GetValue method
         Responsible for returning String values from the configuration file
         Returns the retrieved value if form of a String
        '''
        if self.configLoaded == True:
            # parser helps us retrieve the key for the specified section
            try:
                # return the retrieved key
                return self.parser[section_str][key_str]
            except Exception as e:
                # return false if no key could be retrieved and log the event
                logging.error(e)
                exit(0)
        else:
            # return false if the file has not been loaded
            logging.error("Config File not loaded")
            return False    
  
    def getIntegerValue(self, section_str, key_str) -> int:
        '''
         GetIntegerValue method
         Responsible for returning Integer values from the configuration file
         Returns the retrieved value if it is a Integer, otherwise throws an exception
        '''
        return int(self.getValue(section_str, key_str))  
    
    def getFloatValue(self, section_str, key_str) -> float:
        '''
         GetDoubleValue method
         Responsible for returning floating point values from the configuration file
         Returns the retrieved value if it is a Integer, otherwise throws an exception
        '''
        return float(self.getValue(section_str, key_str))


    def getBooleanValue(self, section_str, key_str):
        '''
         GetBooleanValue method
         Responsible for returning Boolean values from the configuration file
         Returns the retrieved value if it is a Boolean, otherwise returns a null
        '''
        if self.configLoaded == True:
            # parser helps us retrieve the key for the specified section
            # using parser.getboolean we can retrieve a boolean object directly
            try:
                # return the retrieved boolean object
                return self.parser.getboolean(section_str,key_str)
            except Exception as e:
                # return false and log the event if the key could not be retrieved
                logging.error(e) 
                return None
        else:
            #return false if the file has not been loaded
            logging.error("Config File not loaded")
            return None                 
            
    def hasConfigData(self):
        '''
        Method checks if any section in the config has any key.
        Returns a true if yes, else returns a false.
        '''
        if self.configLoaded != False:
            self.sections = list(self.parser.sections())
            # converting the list of key values
            # to a set so we can avoid a double
            # loop when checking if any key exists
            for section in self.sections:                                   
                key_set = set(self.parser[section].values())                
                if len(key_set) > 1 or list(key_set)[0] != 'Not set':       
                    # return true if a unique value is found
                    return True
                else:    
                    # return a false if no unique keys are found and the file is empty
                    return False
        else:
            # return false if the file has not been loaded
            return False   
             
    def loadConfigData(self):
        '''
         LoadConfigData
         This method is responsible for loading the configuration file into the parser
        '''          
        # checking if the file exists                                         
        if os.path.exists(self.filepath):      
            # Loading the file into the parser if it exists then logging and then returning a true                     
            self.parser.read(self.filepath)                         
            self.configLoaded = True  
            return True
        else:    
            # return false if the file has not been loaded
            logging.error("Can not find file: Loading sample file")
            return False  