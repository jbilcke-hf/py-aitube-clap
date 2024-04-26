
def is_valid_number(value):
    """ Check if the value is a valid number """
    try:
        float(value)
        return True
    except (TypeError, ValueError):
        return False
