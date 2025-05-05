# ------------------------------------------
# Authentication Module
# ------------------------------------------

import data_manager

def authenticate_admin():
    """
    Authenticate an administrator using username and password.
    
    Returns:
        bool: True if authentication is successful, False otherwise
    """
    print("\n🔐 Admin Authentication Required 🔐")
    print("---------------------------------")
    
    # Admin credentials
    ADMIN_USERNAME = "1"
    ADMIN_PASSWORD = "12"
    
    # Get admin credentials
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    
    # Validate credentials
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("✅ Admin authentication successful.")
        return True
    else:
        print("🚫 Admin authentication failed.")
        return False

def authenticate_voter(voter_name, signum_credential):
    """
    Authenticate a voter using their name and SIGNUM.
    
    Args:
        voter_name (str): Name of the voter
        signum_credential (str): SIGNUM credential provided by the voter
        
    Returns:
        bool: True if authentication is successful, False otherwise
    """
    if voter_name in data_manager.eligible_voters:
        if signum_credential == data_manager.eligible_voters[voter_name]:
            return True
    return False