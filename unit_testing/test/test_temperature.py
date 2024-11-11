import unittest

from temperature import classify_temperature


class TestClassifyTemperature(unittest.TestCase):

    """
    Test for 'Hypothermia'
    """
    def test_hypothermia(self):
        self.assertEqual(classify_temperature(94), "Hypothermia")

    """Test for 'Low temprature'"""
    def test_low(self):
        self.assertEqual(classify_temperature(96), "Low")

    """Test for 'Normal temprature'"""
    def test_normal(self):
        self.assertEqual(classify_temperature(98), "Normal")

    """Test for 'Elevated temprature'"""
    @unittest.skip("Skip this test")
    def test_elevated(self):
        self.assertEqual(classify_temperature(100), "Elevated")

    """Test for 'Fever'"""
    def test_fever(self):
        self.assertEqual(classify_temperature(101), "Fever")
    
    """Test for 'set of temprature values'"""
    def test_set_of_temprature_values(self):
        test_cases = {
            94: "Hypothermia",
            96: "Low",
            98: "Normal",
            100: "Elevated",
            101: "Fever",
            #99.1: "Fever"
        }
        for temp, expected in test_cases.items():
            # with self.subTest(temp=temp, expected=expected):
                self.assertEqual(classify_temperature(temp), expected)


class TestClassifyTemperatureFractions(unittest.TestCase):
     def test_hypothermia(self):
        self.assertEqual(classify_temperature(94.5), "Hypothermia")


hythermia_test_suite = unittest.TestSuite()
hythermia_test_suite.addTest(TestClassifyTemperature('test_hypothermia'))
hythermia_test_suite.addTest(TestClassifyTemperatureFractions('test_hypothermia'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(hythermia_test_suite)


# if __name__ == '__main__':
#     unittest.main(verbosity=2)

# python -m unittest -v temperature_unit_tests
