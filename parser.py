# parser.py

import re


def extract_emp_id(question: str) -> str:
    question = question.strip()

    # Match patterns like 002516, D002516, DO1917356, EMP123
    match = re.search(r'\b([A-Z]{0,3}\d{4,})\b', question, re.IGNORECASE)

    if match:
        return match.group(1).upper()

    return None
