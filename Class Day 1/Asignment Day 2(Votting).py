# ------------------------------------------
# 🗳️ Enhanced Election Application — Interactive Menu System 🗳️
# ------------------------------------------

# ------------------------------------------
# Functions for Data Management
# ------------------------------------------

def initialize_data():
    """
    Initialize voter credentials and candidate data.
    
    Returns:
        tuple: Contains two dictionaries:
            - voter_database: Dictionary mapping voter names to their SIGNUM credentials
            - candidate_database: Dictionary with candidate names as keys and vote counts as values
    """
    # Database of registered voters with their authentication details
    voter_database = {
        's': 'e', 
        'd': 'r',
        'hindol majumdar': 'ehinmaj', 
        'amrit dash': 'eamdasr', 
        'danish alam a': 'eldaana', 
        'snehasis paloi': 'esnehpa', 
        'arijit mandal': 'earijma', 
        'ajeet kumar sinha': 'eieanjs', 
        'tanweer khan': 'ektahna', 
        'ratnesh kumar r': 'ejlnoow', 
        'subhojit saha': 'eusbash'
    }
    
    # Initial list of candidates with zero votes
    candidate_database = {
        "dup": 0,
        "python": 0,
        "java": 0
    }
    
    return voter_database, candidate_database

# Initialize the main data structures for the election
voter_credentials, candidates = initialize_data()

# Make a copy for tracking who is still eligible to vote
eligible_voters = voter_credentials.copy()
# Dictionary to record which voter voted for which candidate
voting_history = {}  

# ------------------------------------------
# Candidate Management Functions
# ------------------------------------------

def add_candidate():
    """
    Add a new candidate to the election through user input.
    
    Returns:
        str: Status message
    """
    print("\n✨ Add New Candidate ✨")
    print("---------------------")
    
    # Display current candidates
    print("\nCurrent candidates:")
    for candidate_name in candidates.keys():
        print(f"- {candidate_name.title()}")
    
    # Get new candidate name
    new_candidate = input("\nEnter the name of the new candidate: ").lower().strip()
    
    # Validate input
    if not new_candidate:
        return "⚠️ Candidate name cannot be empty."
        
    if new_candidate in candidates:
        return f"⚠️ {new_candidate.title()} is already a candidate."
    
    # Add the new candidate with zero votes
    candidates[new_candidate] = 0
    return f"✅ {new_candidate.title()} has been added as a candidate."

def leader_onboard(candidate_name):
    """
    Add a new candidate to the election.
    
    Args:
        candidate_name (str): Name of the new candidate to add
        
    Returns:
        str: Confirmation message
    """
    candidates.update({candidate_name: 0})
    return "Leader name added"

# ------------------------------------------
# Voter Management Functions
# ------------------------------------------

def add_voter():
    """
    Add a new voter to the election through user input.
    
    Returns:
        str: Status message
    """
    print("\n👤 Add New Voter 👤")
    print("-----------------")
    
    # Get voter details
    new_voter_name = input("Enter the name of the new voter: ").lower().strip()
    
    # Validate input
    if not new_voter_name:
        return "⚠️ Voter name cannot be empty."
        
    if new_voter_name in voter_credentials:
        return f"⚠️ {new_voter_name.title()} is already registered."
    
    # Get SIGNUM credential
    signum = input("Enter the SIGNUM credential for this voter: ").lower().strip()
    
    if not signum:
        return "⚠️ SIGNUM credential cannot be empty."
    
    # Add the new voter
    voter_credentials[new_voter_name] = signum
    eligible_voters[new_voter_name] = signum
    
    return f"✅ {new_voter_name.title()} has been added as a voter with SIGNUM: {signum}"

def authenticate_admin():
    """
    Authenticate an administrator using predefined credentials.
    
    Returns:
        bool: True if authentication is successful, False otherwise
    """
    print("\n🔐 Admin Authentication Required 🔐")
    print("--------------------------------")
    
    # Admin credentials
    ADMIN_USERNAME = "STG"
    ADMIN_PASSWORD = "STG@77"
    
    # Get admin credentials
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    
    # Validate credentials
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("\n✅ Admin authentication successful!")
        return True
    else:
        print("\n❌ Admin authentication failed. Access denied.")
        return False

def remove_voter():
    """
    Remove a voter from the system. Requires admin authentication.
    
    Returns:
        str: Status message
    """
    print("\n❌ Remove Voter ❌")
    print("----------------")
    
    # First authenticate admin
    if not authenticate_admin():
        return "🔒 Operation cancelled: Admin authentication required."
    
    # Show current voters
    print("\nCurrent registered voters:")
    if not voter_credentials:
        return "ℹ️ There are no registered voters to remove."
    
    for voter_name in voter_credentials.keys():
        status = "✅ Has voted" if voter_name in voting_history else "⏳ Not voted yet"
        print(f"- {voter_name.title()} ({status})")
    
    # Get voter to remove
    voter_to_remove = input("\nEnter the name of the voter to remove: ").lower().strip()
    
    # Validate input
    if not voter_to_remove:
        return "⚠️ Voter name cannot be empty."
        
    if voter_to_remove not in voter_credentials:
        return f"⚠️ {voter_to_remove.title()} is not a registered voter."
    
    # Confirm removal
    confirm = input(f"Are you sure you want to remove {voter_to_remove.title()}? (Y/N): ").upper()
    if confirm != "Y":
        return "🛑 Voter removal cancelled."
    
    # Remove the voter
    voter_credentials.pop(voter_to_remove)
    
    # Also remove from eligible voters if they haven't voted yet
    if voter_to_remove in eligible_voters:
        eligible_voters.pop(voter_to_remove)
    
    # Note: We don't remove from voting_history if they've already voted,
    # as that would affect the election integrity
    
    return f"✅ {voter_to_remove.title()} has been removed from the voters list."

# ------------------------------------------
# User Interface and Display Functions
# ------------------------------------------

def display_welcome_message():
    """
    Display the welcome message and list of candidates at the start of the election.
    """
    print("\n🎉 Welcome to the Ericsson MediationElection 🎉\nCandidates standing for election are:\n")
    for candidate in candidates.keys():
        print("-", candidate.title())
    print("\nLet's begin voting! Each voter can vote only once.\n")

def display_candidates():
    """
    Display all available candidates for the election.
    """
    print("Here are the candidates:")
    for candidate in candidates.keys():
        print("-", candidate.title())

def display_results():
    """
    Display the final vote tally for all candidates.
    """
    print("\n📊 Final Vote Tally:")
    for candidate, vote_count in candidates.items():
        print(f"- {candidate.title()}: {vote_count} votes")

def display_voting_history():
    """
    Display the complete voting record showing which voter voted for which candidate.
    """
    print("\n📝 Voting History:")
    for voter_name, candidate_choice in voting_history.items():
        print(f"- {voter_name.title()} voted for {candidate_choice.title()}")

def display_main_menu():
    """
    Display the main menu options for the election system.
    """
    print("\n🗳️ Election System Main Menu 🗳️")
    print("==============================")
    print("1. Start the Election")
    print("2. Add Candidate")
    print("3. Add Voter")
    print("4. Remove Voter (Admin Only)")
    print("5. View Registered Voters")
    print("6. View Candidates")
    print("7. Exit")
    
    choice = input("\nEnter your choice (1-7): ")
    return choice

def view_registered_voters():
    """
    Display all registered voters and their voting status.
    """
    print("\n📋 Registered Voters List 📋")
    print("==========================")
    
    if not voter_credentials:
        print("No voters are registered.")
        return
    
    for voter_name in voter_credentials.keys():
        status = "✅ Has voted" if voter_name in voting_history else "⏳ Not voted yet"
        print(f"- {voter_name.title()} ({status})")

def view_candidates():
    """
    Display all registered candidates.
    """
    print("\n🏆 Registered Candidates 🏆")
    print("==========================")
    
    if not candidates:
        print("No candidates are registered.")
        return
    
    for candidate_name in candidates.keys():
        print(f"- {candidate_name.title()}")

# ------------------------------------------
# Voter Authentication and Validation Functions
# ------------------------------------------

def authenticate_voter(voter_name, signum_credential):
    """
    Authenticate a voter using their name and SIGNUM.
    
    Args:
        voter_name (str): Name of the voter
        signum_credential (str): SIGNUM credential provided by the voter
        
    Returns:
        bool: True if authentication is successful, False otherwise
    """
    if voter_name in eligible_voters:
        if signum_credential == eligible_voters[voter_name]:
            return True
    return False

def is_eligible_to_vote(voter_name):
    """
    Check if a voter is eligible to vote (exists in eligible voters list).
    
    Args:
        voter_name (str): Name of the voter to check
        
    Returns:
        bool: True if voter is eligible, False otherwise
    """
    return voter_name in eligible_voters

def has_already_voted(voter_name):
    """
    Check if a voter has already cast their vote.
    
    Args:
        voter_name (str): Name of the voter to check
        
    Returns:
        bool: True if voter has already voted, False otherwise
    """
    return voter_name in voting_history

def is_valid_candidate(candidate_name):
    """
    Check if the candidate name provided is a valid candidate in the election.
    
    Args:
        candidate_name (str): Name of the candidate to validate
        
    Returns:
        bool: True if candidate exists, False otherwise
    """
    return candidate_name in candidates

# ------------------------------------------
# Voting Process Functions
# ------------------------------------------

def record_vote(voter_name, candidate_name):
    """
    Record a vote for a candidate and update the necessary tracking information.
    
    Args:
        voter_name (str): Name of the voter casting the vote
        candidate_name (str): Name of the candidate receiving the vote
    """
    # Increment the vote count for the selected candidate
    candidates[candidate_name] += 1
    # Record which candidate this voter selected
    voting_history[voter_name] = candidate_name
    # Remove voter from eligible list to prevent re-voting
    eligible_voters.pop(voter_name)

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

    if authenticate_voter(voter_name, signum_credential):
        print("\n✅ Authentication successful! Proceed to vote.")
        display_candidates()
        
        # Vote selection step
        candidate_choice = input("Enter the name of the candidate you wish to vote for:\n").lower()
        vote_confirmation = input(f"You chose {candidate_choice.title()}. Confirm vote? (Y/N): ").lower()
        
        if vote_confirmation != "y":
            print("Vote cancelled.")
            return False
        
        # Vote validation and recording
        if is_valid_candidate(candidate_choice):
            print("\n🎉 Congratulations! Your vote has been cast for", candidate_choice.title())
            record_vote(voter_name, candidate_choice)
            
            # Check if all eligible voters have voted
            if not eligible_voters:
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

# ------------------------------------------
# Results Processing Functions
# ------------------------------------------

def get_max_votes():
    """
    Get the maximum number of votes received by any candidate.
    
    Returns:
        int: The highest vote count
    """
    return max(candidates.values()) if candidates else 0

def find_winners():
    """
    Find the winner(s) of the election based on vote counts.
    
    Returns:
        tuple: Contains:
            - list: Names of candidates with the highest votes
            - int: The maximum vote count
    """
    highest_vote_count = get_max_votes()
    winning_candidates = []
    
    for candidate_name, votes in candidates.items():
        if votes == highest_vote_count:
            winning_candidates.append(candidate_name)
            
    return winning_candidates, highest_vote_count

def declare_winner():
    """
    Declare the winner(s) of the election and handle tie scenarios.
    """
    winning_candidates, highest_vote_count = find_winners()
    
    if not voting_history:
        print("\n⚠️ No votes were cast in this election.")
        return
    
    # Check if there is a single winner or multiple winners (tie)
    if len(winning_candidates) == 1:
        print(f"\n🏆 Winner of the election is: {winning_candidates[0].title()} with {highest_vote_count} votes!")
    else:
        print("\n🤝 It's a tie between the following candidates:")
        for candidate_name in winning_candidates:
            print(f"- {candidate_name.title()} ({candidates[candidate_name]} votes)")

# ------------------------------------------
# Main Program Flow Functions
# ------------------------------------------

def run_election():
    """
    Run the main election process from start to finish.
    """
    # Start with welcome message
    display_welcome_message()
    
    # Validate we have voters and candidates before starting
    if not voter_credentials:
        print("⚠️ There are no registered voters. Please add voters before starting the election.")
        return
        
    if not candidates:
        print("⚠️ There are no registered candidates. Please add candidates before starting the election.")
        return
    
    # Begin the voting loop
    while eligible_voters:
        voter_name = input('\nEnter your name to cast your vote (or type "END" to stop voting):\n').lower()

        # Handle early termination command
        if voter_name == "end":
            if handle_early_termination():
                break
            continue
        
        # Process different voter scenarios
        if is_eligible_to_vote(voter_name):
            # Voter is eligible - process their vote
            process_vote(voter_name)
        elif has_already_voted(voter_name):
            # Voter has already voted
            print(f"⚠️ {voter_name.title()}, you have already cast your vote.")
        else:
            # Voter is not in the system
            print("❌ Your name is not in the voters list.")

    # End the election and show results
    end_election()

def end_election():
    """
    End the election process and display final results and voting history.
    """
    print("\n🔚 Voting session ended. Let's look at the results...\n")
    
    # Show the final results
    display_results()
    declare_winner()
    display_voting_history()

def menu_system():
    """
    Main menu system that controls the flow of the application.
    """
    print("\n🗳️ Welcome to the Ericsson Mediation Election System 🗳️")
    
    while True:
        choice = display_main_menu()
        
        if choice == "1":
            # Start the election
            run_election()
        elif choice == "2":
            # Add candidate
            result = add_candidate()
            print(result)
        elif choice == "3":
            # Add voter
            result = add_voter()
            print(result)
        elif choice == "4":
            # Remove voter (Admin Only)
            result = remove_voter()
            print(result)
        elif choice == "5":
            # View registered voters
            view_registered_voters()
        elif choice == "6":
            # View candidates
            view_candidates()
        elif choice == "7":
            # Exit the system
            print("\n👋 Thank you for using the Election System. Goodbye!")
            break
        else:
            print("\n⚠️ Invalid choice. Please select a number between 1 and 7.")
        
        # Pause before showing the menu again
        input("\nPress Enter to continue...")

# ------------------------------------------
# Start the Election Application
# ------------------------------------------
menu_system()
