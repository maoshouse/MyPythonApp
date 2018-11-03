import json


class Configuration:
    CONFIGURATION_KEY_CITY = "city"
    CONFIGURATION_KEY_COUNTRY = "country"
    MANDATORY_CONFIGURATION_KEYS = {CONFIGURATION_KEY_CITY, CONFIGURATION_KEY_COUNTRY}

    def __init__(self, configuration_json):
        self._configuration = json.loads(configuration_json)
        self._validate_configuration()

    def get_city(self):
        return self._configuration.get(Configuration.CONFIGURATION_KEY_CITY)

    def get_country(self):
        return self._configuration.get(Configuration.CONFIGURATION_KEY_COUNTRY)

    def get_configuration_value(self, key):
        return self._configuration.get(key)

    def _validate_configuration(self):
        if not Configuration.MANDATORY_CONFIGURATION_KEYS.issubset(set(self._configuration)):
            raise KeyError("Configuration is missing required keys!")
