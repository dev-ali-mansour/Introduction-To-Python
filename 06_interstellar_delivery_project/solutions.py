from datetime import datetime,timedelta

def format_date(timestamp,datetime_format):
    dt = datetime.fromtimestamp(timestamp)
    return dt.strftime(datetime_format)

# Example usage
print(format_date(1514665153, "%d-%m-%Y"))

def calculate_landing_time(rocket_launch_dt,travel_duration):
    landing_dt = rocket_launch_dt+timedelta(days = travel_duration)
    return landing_dt.strftime("%d-%m-%Y")

# Example usage
print(calculate_landing_time(datetime(2023, 2, 15), 20))

def days_until_delivery(expected_delivery_dt, current_dt):
    delta = expected_delivery_dt - current_dt
    return delta.days

# Example usage
print(days_until_delivery(datetime(2023, 2, 15), datetime(2023, 2, 5)))