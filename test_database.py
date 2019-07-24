import unittest
import plants
import mongoengine as db


class TestSolution(unittest.TestCase):
    def setUp(self):
        #set up db for testing
        db.connect('gardengraph', host='mongodb://localhost/', port=5000)

    def test_db_plant_creation(unittest.TestCase):
        # Retrieve one random plant from db. Should be a plant object
        self.assertIsInstance()

if __name__ == '__main__':
    # If called like a script, run our tests
    unittest.main()