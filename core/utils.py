import logging
from datetime import datetime

def setup_logging(log_file='trading.log'):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s:%(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

def format_date(dt):
    """Convert datetime to string YYYY-MM-DD"""
    if isinstance(dt, datetime):
        return dt.strftime('%Y-%m-%d')
    return str(dt)

def percentage_change(old, new):
    if old == 0:
        return 0
    return ((new - old) / old) * 100
