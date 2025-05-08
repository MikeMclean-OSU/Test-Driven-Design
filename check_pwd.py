"""Check password function"""

def check_pwd(pwd):
    """Fucntion to verify a password"""
    if len(pwd) >= 8:
        return True
    
    return False
