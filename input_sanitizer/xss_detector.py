from .utils import match_any_pattern

def detect_xss_attack(user_input: str, payloads: list) -> bool:
    xss_keywords = [
        'script', 'iframe', 'onload', 'onerror', 'onclick', 'onmouseover',
        'javascript:', 'alert', 'prompt', 'confirm', 'eval', 'src', 'href', 'style'
    ]
    xss_special_chars = ['<', '>', '"', "'", '&', '(', ')', ';', '{', '}', '[', ']']

    return (
        match_any_pattern(user_input, xss_keywords) or
        match_any_pattern(user_input, xss_special_chars) or
        match_any_pattern(user_input, payloads)
    )
