import unittest
import numpy as np
from src.person import Person

class PersonTest(unittest.TestCase):

    def setUp(self):
        self.person = Person()

        self.ages = np.int32(np.random.normal(loc=45, scale= 30, size=100))

        self.x_values = np.random.uniform(low=0 + 0.1, 
                                            high=1 - 0.1, size=100)
        self.y_values = np.random.uniform(low=0 + 0.1, 
                                            high=1 - 0.1, size=100)

    def tearDown(self):
        pass

    def testSetAge(self):
        self.person.set_age(self.ages)
        self.assertEquals(self.ages.all(), self.person.persons['age'].to_numpy().all())

    def testSetXAxis(self):
        self.person.set_x_axis(self.x_values)
        self.assertEqual(self.x_values.all(), self.person.persons['x_axis'].to_numpy().all())
    
    def testSetYAxis(self):
        self.person.set_y_axis(self.y_values)
        self.assertEqual(self.y_values.all(), self.person.persons['y_axis'].to_numpy().all())

    # def testGetAge(self):
    #     self.person.setYAxis(self.ages)
    #     self.assertEqual(self.ages.all(), self.person.getAge.all())
    
    def testGetXAxis(self):
        self.person.set_x_axis(self.x_values)
        self.assertEqual(self.x_values.all(), self.person.get_x_axis().all())
    
    def testGetYAxis(self):
        self.person.set_y_axis(self.y_values)
        self.assertEqual(self.y_values.all(), self.person.get_y_axis().all())


if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()