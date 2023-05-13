'''
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.
'''

def validate_pin(pin):
    pin_len = len(pin)
    print(pin,pin_len,pin.isnumeric())
    if (pin_len == 4 or pin_len == 6):
        if (pin.isnumeric()):
            return True
    return False