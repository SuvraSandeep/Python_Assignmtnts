# ------------------------------------------
# Voting Process Module
# ------------------------------------------

import data_manager
import auth
import ui
import candidate_manager

def is_eligible_to_vote(voter_name):
    """
    Check if a voter is eligible to vote (exists in eligible voters list).
    
    Args:
        voter_name (str): Name of the voter to check
        
    Returns:
        bool: True if voter is eligible, False otherwise
    """
    return voter_name in data_manager.eligible_voters

def has_already_voted(voter_name):
    """
    Check if a voter has already cast their vote.
    
    Args:
        voter_name (str): Name of the voter to check
        
    Returns:
        bool: True if voter has already voted, False otherwise
    """
    return voter_name in data_manager.voting_history

def record_vote(voter_name, candidate_name):
    """
    Record a vote for a candidate and update the necessary tracking information.
    
    Args:
        voter_name (str): Name of the voter casting the vote
        candidate_name (str): Name of the candidate receiving the vote
    """
    # Increment the vote count for the selected candidate
    data_manager.candidates[candidate_name] += 1
    # Record which candidate this voter selected
    data_manager.voting_history[voter_name] = candidate_name
    # Remove voter from eligible list to prevent re-voting
    data_manager.eligible_voters.pop(voter_name)

def confirm_user_choice(prompt_message):
    """
    Get Y/N confirmation from user with validation.
    
    Args:
        prompt_message (str): Message to display to the user
        
    Returns:
        bool: True for 'Y', False for 'N'
    """
    while True:
        user_choice = input(prompt_message).upper()
        if user_choice in ["Y", "N"]:
            return user_choice == "Y"
        print("⚠️ Invalid input. Please try again.")

def handle_early_termination():
    """
    Handle early termination of voting process when user types "END".
    
    Returns:
        bool: True if voting should end, False if voting should continue
    """
    confirmation_prompt = "\nType 'Y' to end voting and declare results\nOR\nType 'N' to continue voting\n"
    should_terminate = confirm_user_choice(confirmation_prompt)
    
    if not should_terminate:
        print("\n✅ Continuing the voting session...\n")
    
    return should_terminate

def process_vote(voter_name):
    """
    Process a complete voting transaction for a voter.
    
    Args:
        voter_name (str): Name of the voter
        
    Returns:
        bool: True if vote was successfully cast, False otherwise
    """
    # Authentication step
    signum_credential = input("Please enter your SIGNUM for authentication:\n").lower()

    if auth.authenticate_voter(voter_name, signum_credential):
        print("\n✅ Authentication successful! Proceed to vote.")
        ui.display_candidates()
        
        # Vote selection step
        candidate_choice = input("Enter the name of the candidate you wish to vote for:\n").lower()
        vote_confirmation = input(f"You chose {candidate_choice.title()}. Confirm vote? (Y/N): ").lower()
        
        if vote_confirmation != "y":
            print("Vote cancelled.")
            return False
        
        # Vote validation and recording
        if candidate_manager.is_valid_candidate(candidate_choice):
            print("\n🎉 Congratulations! Your vote has been cast for", candidate_choice.title())
            record_vote(voter_name, candidate_choice)
            
            # Check if all eligible voters have voted
            if not data_manager.eligible_voters:
                print("🎯 All voters have completed their voting.")
            else:
                print("\n➡️ Please allow the next voter to proceed.\n")
            return True
        else:
            print("❌ Voting failed: Candidate not recognized.")
            return False
    else:
        print("🚫 Authentication failed: SIGNUM mismatch. Vote not recorded.")
        return False