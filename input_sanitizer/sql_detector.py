from .utils import match_any_pattern

def detect_sql_injection(user_input: str, payloads: list) -> bool:
    keywords = ['select', 'insert', 'update', 'delete', 'drop', 'alter', 'create', 'from', 'where', 'or', 'and', 'union']
    special_chars = ["'", "--", ";", "/*", "*/", "#", "(", ")"]

    return (
        match_any_pattern(user_input, keywords) or
        match_any_pattern(user_input, special_chars) or
        match_any_pattern(user_input, payloads)
    )
