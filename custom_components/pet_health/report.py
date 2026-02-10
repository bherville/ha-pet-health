def generate_markdown_report(pet, weight, visits, recommendation):
    return f"""## {pet} – Health Report

**Weight Avg:** {weight}
**Visits Avg:** {visits}

### Recommendation
{recommendation}

_Not a medical diagnosis._
"""
