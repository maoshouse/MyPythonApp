import copy
import json
import unittest

from model.configuration import Configuration


class ConfigurationTests(unittest.TestCase):
    CITY = "Seattle"
    COUNTRY = "USA"

    BASE_VALID_CONFIGURATION_MAP = {
        Configuration.CONFIGURATION_KEY_CITY: CITY,
        Configuration.CONFIGURATION_KEY_COUNTRY: COUNTRY
    }

    OTHER_KEY = "otherKey"
    OTHER_VALUE = "otherValue"

    BASE_VALID_CONFIGURATION_JSON = json.dumps(BASE_VALID_CONFIGURATION_MAP)
    INVALID_CONFIGURATION_JSON = json.dumps({})

    def setUp(self):
        self.configuration = Configuration(ConfigurationTests.BASE_VALID_CONFIGURATION_JSON)

    def test_invalid_configuration(self):
        self.assertRaises(KeyError, Configuration, self.INVALID_CONFIGURATION_JSON)

    def test_get_city(self):
        self.assertEqual(self.CITY, self.configuration.get_city())

    def test_get_country(self):
        self.assertEqual(self.COUNTRY, self.configuration.get_country())

    def test_get_other_configuration_value(self):
        extended_configuration_map = copy.deepcopy(ConfigurationTests.BASE_VALID_CONFIGURATION_MAP)
        extended_configuration_map.update({ConfigurationTests.OTHER_KEY: ConfigurationTests.OTHER_VALUE})
        extended_configuration_json = json.dumps(extended_configuration_map)
        configuration = Configuration(extended_configuration_json)

        self.assertEqual(ConfigurationTests.OTHER_VALUE,
                         configuration.get_configuration_value(ConfigurationTests.OTHER_KEY))
