def match_any_pattern(user_input: str, pattern_list: list) -> bool:
    input_lower = user_input.lower()
    return any(pattern.lower() in input_lower for pattern in pattern_list)
