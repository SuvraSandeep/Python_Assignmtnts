# ------------------------------------------
# Voter Management Module
# ------------------------------------------

import data_manager
import auth

def add_voter():
    """
    Add a new voter to the election through user input after admin authentication.
    
    Returns:
        str: Status message
    """
    print("\n👤 Add New Voter 👤")
    print("-----------------")
    
    # First authenticate as admin
    if not auth.authenticate_admin():
        return "🚫 Access denied. Admin authentication required to add voters."
    
    # Get voter details
    new_voter_name = input("Enter the name of the new voter: ").lower().strip()
    
    # Validate input
    if not new_voter_name:
        return "⚠️ Voter name cannot be empty."
        
    if new_voter_name in data_manager.voter_credentials:
        return f"⚠️ {new_voter_name.title()} is already registered."
    
    # Get SIGNUM credential
    signum = input("Enter the SIGNUM credential for this voter: ").lower().strip()
    
    if not signum:
        return "⚠️ SIGNUM credential cannot be empty."
    
    # Add the new voter
    data_manager.voter_credentials[new_voter_name] = signum
    data_manager.eligible_voters[new_voter_name] = signum
    
    return f"✅ {new_voter_name.title()} has been added as a voter with SIGNUM: {signum}"

def remove_voter():
    """
    Remove a voter from the election system after admin authentication.
    
    Returns:
        str: Status message
    """
    print("\n❌ Remove Voter ❌")
    print("----------------")
    
    # First authenticate as admin
    if not auth.authenticate_admin():
        return "🚫 Access denied. Admin authentication required to remove voters."
    
    # Show current voters
    print("\nCurrent registered voters:")
    for voter_name in data_manager.voter_credentials.keys():
        status = "✅ Has voted" if voter_name in data_manager.voting_history else "⏳ Not voted yet"
        print(f"- {voter_name.title()} ({status})")
    
    # Get voter to remove
    voter_to_remove = input("\nEnter the name of the voter to remove: ").lower().strip()
    
    # Validate input
    if not voter_to_remove:
        return "⚠️ Voter name cannot be empty."
        
    if voter_to_remove not in data_manager.voter_credentials:
        return f"⚠️ {voter_to_remove.title()} is not in the registered voters list."
    
    # Check if voter has already voted
    if voter_to_remove in data_manager.voting_history:
        confirm = input(f"⚠️ WARNING: {voter_to_remove.title()} has already voted. Removing will affect election results. Continue? (Y/N): ").upper()
        if confirm != "Y":
            return "Voter removal cancelled."
        
        # Remove their vote
        voted_for = data_manager.voting_history[voter_to_remove]
        data_manager.candidates[voted_for] -= 1
        del data_manager.voting_history[voter_to_remove]
    
    # Remove from voter lists
    del data_manager.voter_credentials[voter_to_remove]
    if voter_to_remove in data_manager.eligible_voters:
        del data_manager.eligible_voters[voter_to_remove]
    
    return f"✅ {voter_to_remove.title()} has been removed from the voter registry."