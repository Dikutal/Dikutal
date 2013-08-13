def datetime_to_date(dt):
    if dt is not None:
        return date(dt.year, dt.month, dt.day)
