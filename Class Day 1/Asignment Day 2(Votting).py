# ------------------------------------------
# 🗳️ Enhanced Election Application — Interactive Menu System 🗳️
# ------------------------------------------

# ------------------------------------------
# Functions for Data Management
# ------------------------------------------

def initialize_data():
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
# Authentication Functions
# ------------------------------------------

def authenticate_admin():
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

# ------------------------------------------
# Candidate Management Functions
# ------------------------------------------

def add_candidate():
    print("\n✨ Add New Candidate ✨")
    print("---------------------")
    
    # First authenticate as admin
    if not authenticate_admin():
        return "🚫 Access denied. Admin authentication required to add candidates."
    
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

def remove_candidate():

    print("\n❌ Remove Candidate ❌")
    print("-------------------")
    
    # First authenticate as admin
    if not authenticate_admin():
        return "🚫 Access denied. Admin authentication required to remove candidates."
    
    # Show current candidates
    print("\nCurrent candidates:")
    for candidate_name, votes in candidates.items():
        print(f"- {candidate_name.title()} (Current votes: {votes})")
    
    # Get candidate to remove
    candidate_to_remove = input("\nEnter the name of the candidate to remove: ").lower().strip()
    
    # Validate input
    if not candidate_to_remove:
        return "⚠️ Candidate name cannot be empty."
        
    if candidate_to_remove not in candidates:
        return f"⚠️ {candidate_to_remove.title()} is not in the candidates list."
    
    # Check if candidate has votes
    if candidates[candidate_to_remove] > 0:
        confirm = input(f"⚠️ WARNING: {candidate_to_remove.title()} has {candidates[candidate_to_remove]} votes. Removing will affect election results. Continue? (Y/N): ").upper()
        if confirm != "Y":
            return "Candidate removal cancelled."
        
        # Need to update voting history to remove references to this candidate
        voters_affected = [voter for voter, candidate in voting_history.items() if candidate == candidate_to_remove]
        for voter in voters_affected:
            del voting_history[voter]
            # Make these voters eligible to vote again
            if voter in voter_credentials:
                eligible_voters[voter] = voter_credentials[voter]
    
    # Remove the candidate
    del candidates[candidate_to_remove]
    
    return f"✅ {candidate_to_remove.title()} has been removed from the candidates list."

def leader_onboard(candidate_name):

    candidates.update({candidate_name: 0})
    return "Leader name added"

# ------------------------------------------
# Voter Management Functions
# ------------------------------------------

def add_voter():

    print("\n👤 Add New Voter 👤")
    print("-----------------")
    
    # First authenticate as admin
    if not authenticate_admin():
        return "🚫 Access denied. Admin authentication required to add voters."
    
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

def remove_voter():

    print("\n❌ Remove Voter ❌")
    print("----------------")
    
    # First authenticate as admin
    if not authenticate_admin():
        return "🚫 Access denied. Admin authentication required to remove voters."
    
    # Show current voters
    print("\nCurrent registered voters:")
    for voter_name in voter_credentials.keys():
        status = "✅ Has voted" if voter_name in voting_history else "⏳ Not voted yet"
        print(f"- {voter_name.title()} ({status})")
    
    # Get voter to remove
    voter_to_remove = input("\nEnter the name of the voter to remove: ").lower().strip()
    
    # Validate input
    if not voter_to_remove:
        return "⚠️ Voter name cannot be empty."
        
    if voter_to_remove not in voter_credentials:
        return f"⚠️ {voter_to_remove.title()} is not in the registered voters list."
    
    # Check if voter has already voted
    if voter_to_remove in voting_history:
        confirm = input(f"⚠️ WARNING: {voter_to_remove.title()} has already voted. Removing will affect election results. Continue? (Y/N): ").upper()
        if confirm != "Y":
            return "Voter removal cancelled."
        
        # Remove their vote
        voted_for = voting_history[voter_to_remove]
        candidates[voted_for] -= 1
        del voting_history[voter_to_remove]
    
    # Remove from voter lists
    del voter_credentials[voter_to_remove]
    if voter_to_remove in eligible_voters:
        del eligible_voters[voter_to_remove]
    
    return f"✅ {voter_to_remove.title()} has been removed from the voter registry."

# ------------------------------------------
# User Interface and Display Functions
# ------------------------------------------

def display_welcome_message():

    print("\n🎉 Welcome to the Ericsson MediationElection 🎉\nCandidates standing for election are:\n")
    for candidate in candidates.keys():
        print("-", candidate.title())
    print("\nLet's begin voting! Each voter can vote only once.\n")

def display_candidates():

    print("Here are the candidates:")
    for candidate in candidates.keys():
        print("-", candidate.title())

def display_results():

    print("\n📊 Final Vote Tally:")
    for candidate, vote_count in candidates.items():
        print(f"- {candidate.title()}: {vote_count} votes")

def display_voting_history():

    print("\n📝 Voting History:")
    for voter_name, candidate_choice in voting_history.items():
        print(f"- {voter_name.title()} voted for {candidate_choice.title()}")

def display_main_menu():

    print("\n🗳️ Election System Main Menu 🗳️")
    print("==============================")
    print("1. Start the Election")
    print("2. Admin Menu (Authentication Required)")
    print("3. View Registered Voters")
    print("4. View Candidates")
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5): ")
    return choice

def display_admin_menu():

    print("\n👑 Admin Control Panel 👑")
    print("=======================")
    print("1. Add Candidate")
    print("2. Remove Candidate")
    print("3. Add Voter")
    print("4. Remove Voter")
    print("5. Return to Main Menu")
    
    choice = input("\nEnter your choice (1-5): ")
    return choice

def view_registered_voters():

    print("\n📋 Registered Voters List 📋")
    print("==========================")
    
    if not voter_credentials:
        print("No voters are registered.")
        return
    
    for voter_name in voter_credentials.keys():
        status = "✅ Has voted" if voter_name in voting_history else "⏳ Not voted yet"
        print(f"- {voter_name.title()} ({status})")

def view_candidates():

    print("\n🏆 Registered Candidates 🏆")
    print("==========================")
    
    if not candidates:
        print("No candidates are registered.")
        return
    
    for candidate_name, votes in candidates.items():
        print(f"- {candidate_name.title()} (Current votes: {votes})")

# ------------------------------------------
# Voter Authentication and Validation Functions
# ------------------------------------------

def authenticate_voter(voter_name, signum_credential):
    if voter_name in eligible_voters:
        if signum_credential == eligible_voters[voter_name]:
            return True
    return False

def is_eligible_to_vote(voter_name):

    return voter_name in eligible_voters

def has_already_voted(voter_name):

    return voter_name in voting_history

def is_valid_candidate(candidate_name):

    return candidate_name in candidates

# ------------------------------------------
# Voting Process Functions
# ------------------------------------------

def record_vote(voter_name, candidate_name):

    # Increment the vote count for the selected candidate
    candidates[candidate_name] += 1
    # Record which candidate this voter selected
    voting_history[voter_name] = candidate_name
    # Remove voter from eligible list to prevent re-voting
    eligible_voters.pop(voter_name)

def confirm_user_choice(prompt_message):

    while True:
        user_choice = input(prompt_message).upper()
        if user_choice in ["Y", "N"]:
            return user_choice == "Y"
        print("⚠️ Invalid input. Please try again.")

def handle_early_termination():

    confirmation_prompt = "\nType 'Y' to end voting and declare results\nOR\nType 'N' to continue voting\n"
    should_terminate = confirm_user_choice(confirmation_prompt)
    
    if not should_terminate:
        print("\n✅ Continuing the voting session...\n")
    
    return should_terminate

def process_vote(voter_name):

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

    return max(candidates.values()) if candidates else 0

def find_winners():

    highest_vote_count = get_max_votes()
    winning_candidates = []
    
    for candidate_name, votes in candidates.items():
        if votes == highest_vote_count:
            winning_candidates.append(candidate_name)
            
    return winning_candidates, highest_vote_count

def declare_winner():

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

    print("\n🔚 Voting session ended. Let's look at the results...\n")
    
    # Show the final results
    display_results()
    declare_winner()
    display_voting_history()

def admin_menu_system():

    # First authenticate as admin
    if not authenticate_admin():
        print("🚫 Access denied. Admin authentication required to access the admin menu.")
        return
    
    while True:
        choice = display_admin_menu()
        
        if choice == "1":
            # Add candidate
            result = add_candidate()  # Skip auth since we already authenticated
            print(result)
        elif choice == "2":
            # Remove candidate
            result = remove_candidate()  # Skip auth since we already authenticated
            print(result)
        elif choice == "3":
            # Add voter
            result = add_voter()  # Skip auth since we already authenticated
            print(result)
        elif choice == "4":
            # Remove voter
            result = remove_voter()  # Skip auth since we already authenticated
            print(result)
        elif choice == "5":
            # Return to main menu
            print("\n🔙 Returning to main menu...")
            break
        else:
            print("\n⚠️ Invalid choice. Please select a number between 1 and 5.")
        
        # Pause before showing the admin menu again
        input("\nPress Enter to continue...")

def menu_system():

    print("\n🗳️ Welcome to the Ericsson Mediation Election System 🗳️")
    
    while True:
        choice = display_main_menu()
        
        if choice == "1":
            # Start the election
            run_election()
        elif choice == "2":
            # Enter admin menu
            admin_menu_system()
        elif choice == "3":
            # View registered voters
            view_registered_voters()
        elif choice == "4":
            # View candidates
            view_candidates()
        elif choice == "5":
            # Exit the system
            print("\n👋 Thank you for using the Election System. Goodbye!")
            break
        else:
            print("\n⚠️ Invalid choice. Please select a number between 1 and 5.")
        
        # Pause before showing the menu again
        input("\nPress Enter to continue...")

# ------------------------------------------
# Start the Election Application
# ------------------------------------------
menu_system()
