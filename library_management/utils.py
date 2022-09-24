import pyotp

def get_otp():
    base32secret = pyotp.random_base32()
    totp = pyotp.TOTP(base32secret, interval=600)
    otp = totp.now()
    return {"secret":base32secret, "otp":otp}