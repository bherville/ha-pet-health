from homeassistant.helpers.entity import BinarySensorEntity

class PetHealthAnomalyBinary(BinarySensorEntity):
    def __init__(self, score_sensor, threshold=2.5):
        self._score_sensor = score_sensor
        self._threshold = threshold
        self._attr_name = f"{score_sensor.name} Alert"

    @property
    def is_on(self):
        try:
            return abs(float(self._score_sensor.state)) >= self._threshold
        except Exception:
            return False
