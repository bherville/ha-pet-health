from homeassistant.helpers.entity import SensorEntity
from homeassistant.components.recorder.history import get_significant_states
from homeassistant.util import dt as dt_util
from datetime import timedelta
import statistics

class PetHealthAnomalyScoreSensor(SensorEntity):
    def __init__(self, hass, name, entity_id):
        self.hass = hass
        self._entity_id = entity_id
        self._attr_name = f"{name} Anomaly Score"
        self._state = 0

    async def async_update(self):
        end = dt_util.utcnow()
        start = end - timedelta(days=7)

        states = await self.hass.async_add_executor_job(
            get_significant_states,
            self.hass,
            start,
            end,
            [self._entity_id],
            True
        )

        history = [
            float(s.state)
            for s in states.get(self._entity_id, [])
            if s.state.replace(".", "", 1).isdigit()
        ]

        if len(history) < 10:
            self._state = 0
            return

        mean = statistics.mean(history)
        std = statistics.stdev(history) or 0.01
        self._state = round((history[-1] - mean) / std, 2)

    @property
    def state(self):
        return self._state
