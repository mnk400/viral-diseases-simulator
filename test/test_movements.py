"""
Test file for the movements class.

Created on Dec 4th, 2020
@author: manik
"""

import unittest
from src.movements import Movement
import src.person_properties_util as idx
from src.population import Population
import numpy as np


class MovementTest(unittest.TestCase):

    def setUp(self) -> None:
        self.pop      = Population(size=10)
        self.movement = Movement()

    def tearDown(self) -> None:
        self.pop = None
        self.movement = None
        pass

    def test_update_person(self) -> None:
        """
        Tests update person to check data is getting 
        updated randomly
        """

        self.assertIsInstance(self.movement.update_persons(self.pop.get_person(),len(self.pop.get_person())), np.ndarray)
        self.pop.persons[:,idx.speed] = 0.1
        self.assertNotEqual(self.movement.update_persons(self.pop.get_person(),
            len(self.pop.get_person()),heading_update_chance=1)[:,idx.y_dir].any(), 0)
        self.assertNotEqual(self.movement.update_persons(self.pop.get_person(),
            len(self.pop.get_person()),heading_update_chance=1)[:,idx.x_dir].any(), 0)
        self.assertNotEqual(self.movement.update_persons(self.pop.get_person(),
            len(self.pop.get_person()),heading_update_chance=1)[:,idx.speed].any(), 0.1)

    def test_out_of_bounds(self) -> None:
        """
        Tests out_of_bounds function to check directions 
        are updated when a person is heading out of bounds
        """

        self.assertIsInstance(self.movement.out_of_bounds(self.pop.get_person(),
            np.array([[0,1]] * 10),np.array([[0,1]] * 10)), np.ndarray)
        self.pop.persons[:,idx.speed] = 1
        self.pop.persons[:,idx.x_axis] = 1.1
        self.pop.persons[:,idx.y_axis] = 1.1
        self.pop.persons[:,idx.x_dir] = 0.5
        self.pop.persons[:,idx.y_dir] = 0.5

        self.assertLess(list(self.movement.out_of_bounds(self.pop.get_person(),
             np.array([[0,1]] * 10),np.array([[0,1]] * 10))[:,idx.x_dir]), [0]*10)
        self.assertLess(list(self.movement.out_of_bounds(self.pop.get_person(),
             np.array([[0,1]] * 10),np.array([[0,1]] * 10))[:,idx.x_dir]), [0]*10)

        self.pop.persons[:,idx.x_axis] = -0.1
        self.pop.persons[:,idx.y_axis] = -0.1
        self.pop.persons[:,idx.x_dir] = -0.5
        self.pop.persons[:,idx.y_dir] = -0.5
        self.assertGreater(list(self.movement.out_of_bounds(self.pop.get_person(),
             np.array([[0,1]] * 10),np.array([[0,1]] * 10))[:,idx.x_dir]), [0]*10)
        self.assertGreater(list(self.movement.out_of_bounds(self.pop.get_person(),
             np.array([[0,1]] * 10),np.array([[0,1]] * 10))[:,idx.x_dir]), [0]*10)

    def test_update_pop(self) -> None:
        """
        Tests the update_pop function
        """
        
        self.pop.persons[:,idx.x_dir] = 0.1
        self.pop.persons[:,idx.y_dir] = 0.1
        self.pop.persons[:,idx.speed] = 1

        expectd_x = list(self.pop.persons[:,idx.x_axis] + 0.1)
        expectd_y = list(self.pop.persons[:,idx.y_axis] + 0.1)
        
        self.pop.persons = self.movement.update_pop(self.pop.persons)

        self.assertIsInstance(self.pop.get_person(), np.ndarray)
        self.assertListEqual(list(self.pop.get_x_axis()),expectd_x)
        self.assertListEqual(list(self.pop.get_y_axis()),expectd_y)
