from homeassistant import config_entries
from homeassistant.helpers.selector import selector
from .const import DOMAIN

class PetHealthConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(
                title=user_input["pet_name"],
                data=user_input
            )

        return self.async_show_form(
            step_id="user",
            data_schema={
                "pet_name": str,
                "weight_sensor": selector({"entity": {"domain": "sensor"}}),
                "visits_sensor": selector({"entity": {"domain": "sensor"}}),
            }
        )
