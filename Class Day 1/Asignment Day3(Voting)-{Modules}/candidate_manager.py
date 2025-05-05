# ------------------------------------------
# Candidate Management Module
# ------------------------------------------

import data_manager
import auth

def add_candidate():
    """
    Add a new candidate to the election through user input after admin authentication.
    
    Returns:
        str: Status message
    """
    print("\n✨ Add New Candidate ✨")
    print("---------------------")
    
    # First authenticate as admin
    if not auth.authenticate_admin():
        return "🚫 Access denied. Admin authentication required to add candidates."
    
    # Display current candidates
    print("\nCurrent candidates:")
    for candidate_name in data_manager.candidates.keys():
        print(f"- {candidate_name.title()}")
    
    # Get new candidate name
    new_candidate = input("\nEnter the name of the new candidate: ").lower().strip()
    
    # Validate input
    if not new_candidate:
        return "⚠️ Candidate name cannot be empty."
        
    if new_candidate in data_manager.candidates:
        return f"⚠️ {new_candidate.title()} is already a candidate."
    
    # Add the new candidate with zero votes
    data_manager.candidates[new_candidate] = 0
    return f"✅ {new_candidate.title()} has been added as a candidate."

def remove_candidate():
    """
    Remove a candidate from the election system after admin authentication.
    
    Returns:
        str: Status message
    """
    print("\n❌ Remove Candidate ❌")
    print("-------------------")
    
    # First authenticate as admin
    if not auth.authenticate_admin():
        return "🚫 Access denied. Admin authentication required to remove candidates."
    
    # Show current candidates
    print("\nCurrent candidates:")
    for candidate_name, votes in data_manager.candidates.items():
        print(f"- {candidate_name.title()} (Current votes: {votes})")
    
    # Get candidate to remove
    candidate_to_remove = input("\nEnter the name of the candidate to remove: ").lower().strip()
    
    # Validate input
    if not candidate_to_remove:
        return "⚠️ Candidate name cannot be empty."
        
    if candidate_to_remove not in data_manager.candidates:
        return f"⚠️ {candidate_to_remove.title()} is not in the candidates list."
    
    # Check if candidate has votes
    if data_manager.candidates[candidate_to_remove] > 0:
        confirm = input(f"⚠️ WARNING: {candidate_to_remove.title()} has {data_manager.candidates[candidate_to_remove]} votes. Removing will affect election results. Continue? (Y/N): ").upper()
        if confirm != "Y":
            return "Candidate removal cancelled."
        
        # Need to update voting history to remove references to this candidate
        voters_affected = [voter for voter, candidate in data_manager.voting_history.items() if candidate == candidate_to_remove]
        for voter in voters_affected:
            del data_manager.voting_history[voter]
            # Make these voters eligible to vote again
            if voter in data_manager.voter_credentials:
                data_manager.eligible_voters[voter] = data_manager.voter_credentials[voter]
    
    # Remove the candidate
    del data_manager.candidates[candidate_to_remove]
    
    return f"✅ {candidate_to_remove.title()} has been removed from the candidates list."

def leader_onboard(candidate_name):
    """
    Add a new candidate to the election.
    
    Args:
        candidate_name (str): Name of the new candidate to add
        
    Returns:
        str: Confirmation message
    """
    data_manager.candidates.update({candidate_name: 0})
    return "Leader name added"

def is_valid_candidate(candidate_name):
    """
    Check if the candidate name provided is a valid candidate in the election.
    
    Args:
        candidate_name (str): Name of the candidate to validate
        
    Returns:
        bool: True if candidate exists, False otherwise
    """
    return candidate_name in data_manager.candidates