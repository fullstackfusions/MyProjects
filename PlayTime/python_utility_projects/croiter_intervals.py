from croniter import croniter
from datetime import datetime

def generate_intervals(cron_expression: str, start_date: datetime, end_date: datetime):
    """
    Generates a list of (start_time, end_time) tuples based on the given cron expression.

    Args:
        cron_expression (str): A valid cron expression for the intervals.
        start_date (datetime): The start date for the intervals.
        end_date (datetime): The end date for the intervals.

    Returns:
        List[Tuple[datetime, datetime]]: A list of (start_time, end_time) tuples.
    """
    cron_iter = croniter(cron_expression, start_date)
    intervals = []

    while True:
        next_start = cron_iter.get_next(datetime)
        if next_start >= end_date:
            break
        next_end = cron_iter.get_next(datetime)
        if next_end > end_date:
            next_end = end_date
        intervals.append((next_start, next_end))

    return intervals


# # One month of interval
# cron_expression = "0 0 1 * *"  # First day of every month
# start_date = datetime(2024, 1, 1)
# end_date = datetime(2024, 12, 31)
# intervals = generate_intervals(cron_expression, start_date, end_date)
# print(len(intervals))

# # One day interval
# cron_expression = "0 0 * * *"  # Start of every day
# start_date = datetime(2024, 11, 1)
# end_date = datetime(2024, 11, 30)
# intervals = generate_intervals(cron_expression, start_date, end_date)
# print(len(intervals))

# # One hour interval
# cron_expression = "0 * * * *"  # Every hour
# start_date = datetime(2024, 11, 1)
# end_date = datetime(2024, 11, 2)  # One day range
# intervals = generate_intervals(cron_expression, start_date, end_date)
# print(len(intervals))

# # 6 hours interval
# cron_expression = "0 */6 * * *"  # Every 6 hours
# start_date = datetime(2024, 11, 1)
# end_date = datetime(2024, 11, 3)
# intervals = generate_intervals(cron_expression, start_date, end_date)
# print(len(intervals))

# # 6 days interval
# cron_expression = "0 0 */6 * *"  # Every 6 days
# start_date = datetime(2024, 11, 1)
# end_date = datetime(2024, 12, 1)
# intervals = generate_intervals(cron_expression, start_date, end_date)
# print(len(intervals))

# # 6 months interval
# cron_expression = "0 0 1 */6 *"  # Every 6 months
# start_date = datetime(2024, 1, 1)
# end_date = datetime(2025, 1, 1)
# intervals = generate_intervals(cron_expression, start_date, end_date)
# print(len(intervals))

# # 5 minutes interval
# cron_expression = "*/5 * * * *"  # Every 5 minutes
# start_date = datetime(2024, 11, 1)
# end_date = datetime(2024, 12, 1)
# intervals = generate_intervals(cron_expression, start_date, end_date)
# print(len(intervals))
