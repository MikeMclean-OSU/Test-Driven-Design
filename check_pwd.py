"""Check password function"""

def check_pwd(pwd):
    """Fucntion to verify a password"""
    if len(pwd) >= 8 and len(pwd) <= 20:
        return True

    return False
