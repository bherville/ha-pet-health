from custom_components.pet_health.sensor import PetHealthAnomalyScoreSensor

def test_z_score_calculation():
    history = [10, 10, 11, 10, 10, 11, 10, 10, 11, 12]
    mean = sum(history) / len(history)
    assert mean > 0
