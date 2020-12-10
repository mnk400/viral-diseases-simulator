"""
Test file for config util class

Created on Dec 2nd, 2020
@author: Yatish Pitta
"""

import logging
import unittest
from src.config_util import ConfigUtil
import json


class ConfigUtilClassTest(unittest.TestCase):
    """
    Test cases to test the methods of the ConfigUtil class
    """

    def setUp(self) -> None:
        """
        Setup method initializes an instance of ConfigUtil class
        """
        logging.basicConfig(format='\n%(asctime)s:%(module)s:%(levelname)s:%(message)s', level=logging.DEBUG)
        logging.info('Testing ConfigUtil class.....')
        self.config_util = ConfigUtil('config/test_config.ini')

    def test_get_value(self):
        """
        Tests the getValue() method to see if the method is able to obtain the String value from the config file using the section and key given
        """
        self.assertIsInstance(self.config_util.getValue("virus.stats", "k_value"), str)
        self.assertEqual(self.config_util.getValue("virus.stats", "k_value"), str(0.1))

    def test_get_integer(self):
        """
        Tests the getIntegerValue() method to see if the method is able to obtain the int value from the config file using the section and key given
        """
        self.assertIsInstance(self.config_util.getIntegerValue("virus.stats", "r_value"), int)
        self.assertEqual(self.config_util.getIntegerValue("virus.stats", "r_value"), 3)

    def test_get_float(self):
        """
        Tests the getFloatValue() method to see if the method is able to obtain the float value from the config file using the section and key given
        """
        self.assertIsInstance(self.config_util.getFloatValue("virus.stats", "r_value"), float)
        self.assertEqual(self.config_util.getFloatValue("virus.stats", "k_value"), 0.1)

    def test_get_dictionary(self):
        """
        Tests the getDictionary method to see if the method is able to obtain the json string from the config file and convert it to dictionary type using the section and key given
        """
        self.assertIsInstance(self.config_util.getDictionary("virus.stats", "mortality_rate"), dict)
        self.assertEqual(self.config_util.getDictionary("virus.stats", "mortality_rate"), json.loads(self.config_util.getValue("virus.stats", "mortality_rate")))

    def test_get_boolean(self):
        """
        Tests the getBooleanValue() method to see if the method is able to obtain the boolean value from the config file using the section and key given
        """
        self.assertIsInstance(self.config_util.getBooleanValue("people.stats", "use_masks"), bool)
        self.assertEqual(self.config_util.getBooleanValue("people.stats", "use_masks"), True)

    def test_support_methods(self):
        """
        Tests the hasConfigData() and loadConfigData() methods to check if they are able to load the config file if valid and indicate failure if file not valid
        """
        self.assertTrue(self.config_util.hasConfigData())
        self.assertTrue(self.config_util.loadConfigData())

        wrong_config = ConfigUtil('config/wrong_file')

        self.assertFalse(wrong_config.hasConfigData())
        self.assertFalse(wrong_config.loadConfigData())