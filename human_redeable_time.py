'''
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
'''


from datetime import datetime

def make_readable(seconds):
    if (seconds > 359999):
        return 0
    hours = int(seconds / 3600)
    hours = f"{hours:0>2}"
    seconds = seconds % 3600
    minutes = int(seconds / 60)
    minutes = f"{minutes:0>2}"
    seconds = seconds % 60
    seconds = f"{seconds:0>2}"
    return f"{hours}:{minutes}:{seconds}"