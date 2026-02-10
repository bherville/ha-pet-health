def generate_markdown_report(pet_name, weight_avg, visits_avg, recommendation):
    return f"""## {pet_name} – Health Report

**Average Weight:** {weight_avg}
**Average Visits / Day:** {visits_avg}

### Recommendation
{recommendation}

_Not a medical diagnosis._
"""
