from homeassistant.helpers.entity import SensorEntity
from homeassistant.const import STATE_UNKNOWN
import statistics

class PetHealthAnomalyScoreSensor(SensorEntity):
    def __init__(self, name, source_entity, history):
        self._attr_name = f"{name} Anomaly Score"
        self._source = source_entity
        self._history = history
        self._state = 0

    def update(self):
        try:
            values = [float(v) for v in self._history if v not in (None, STATE_UNKNOWN)]
            if len(values) < 10:
                self._state = 0
                return
            avg = statistics.mean(values)
            std = statistics.stdev(values) or 0.01
            current = values[-1]
            self._state = round((current - avg) / std, 2)
        except Exception:
            self._state = 0

    @property
    def state(self):
        return self._state
