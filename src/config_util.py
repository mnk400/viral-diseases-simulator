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
    This class is responsible for reading and parsing the configuration files.
    Apache.commons.configuration is used to parse the files.
    '''

    #Singleton instance for ConfigUtil class
    _instance = ()          

    def getInstance():
        """
        This class returns the singleton instance of the ConfigUtil class

        Returns
        -------
        ConfigUtil
            The singleton instance of the ConfigUtil class
        """        
        return ConfigUtil._instance
    
    def __init__(self, path_param: str):
        """
        Constructor responsible for calling the load function to load configuration data from the file.
        This constructor loads the default specified path as the config file if no other file path is input.

        Parameters
        ----------
        path_param : str
            Relative path to the configuration file
        """        
        self.parser = configparser.ConfigParser()
        self.filepath = path_param

        # Path to the configuration file from current dir
        self.configLoaded = False
        self.loadConfigData()

    def getValue(self, section_str: str, key_str: str) -> str:
        """
        Responsible for returning string values from the configuration file

        Parameters
        ----------
        section_str : str
            The section in the configuration file to get the value from
        key_str : str
            The corresponding key to get the value from

        Returns
        -------
        str
            The string value corresponding to the section and key
        """        

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
        """
        Responsible for returning int values from the configuration file, throws an exception
        if the value is not an integer

        Parameters
        ----------
        section_str : str
            The section in the configuration file to get the value from
        key_str : str
            The corresponding key to get the value from

        Returns
        -------
        int
            The integer value corresponding to the section and key
        """ 
        return int(self.getValue(section_str, key_str))  
    
    def getFloatValue(self, section_str, key_str) -> float:
        """
        Responsible for returning float values from the configuration file, throws an exception
        if the value is not a float

        Parameters
        ----------
        section_str : str
            The section in the configuration file to get the value from
        key_str : str
            The corresponding key to get the value from

        Returns
        -------
        float
            The float value corresponding to the section and key
        """ 
        return float(self.getValue(section_str, key_str))

    def getBooleanValue(self, section_str, key_str) -> bool:
        """
        Responsible for returning bool values from the configuration file, throws an exception
        if the value is not a bool

        Parameters
        ----------
        section_str : str
            The section in the configuration file to get the value from
        key_str : str
            The corresponding key to get the value from

        Returns
        -------
        float
            The bool value corresponding to the section and key
        """ 
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
            
    def hasConfigData(self) -> bool:
        """
        Method checks if any section in the config has any key.

        Returns
        -------
        bool
            Returns if any section in the config file is non-empty
        """ 
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
        """
        Method responsible for loading the config file

        Returns
        -------
        bool
            Indicates whether loading the config file was successful or not
        """          
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