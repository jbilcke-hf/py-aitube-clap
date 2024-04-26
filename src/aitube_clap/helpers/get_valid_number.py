def get_valid_number(value, min_value, max_value, default):
    try:
        num = int(value)
        if min_value <= num <= max_value:
            return num
    except (TypeError, ValueError):
        pass
    return default
