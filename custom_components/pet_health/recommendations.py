def generate_recommendation(weight, visits, baseline_weight):
    if visits > 6:
        return "Increase hydration and monitor urinary health."
    if weight > baseline_weight + 1:
        return "Review feeding portions and activity levels."
    return "No action needed."
