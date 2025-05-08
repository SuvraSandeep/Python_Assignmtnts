# ------------------------------------------
# User Interface Module
# ------------------------------------------

import data_manager
import results

def display_welcome_message():
    """
    Display the welcome message and list of candidates at the start of the election.
    """
    print("\n🎉 Welcome to the Ericsson MediationElection 🎉\nCandidates standing for election are:\n")
    for candidate in data_manager.candidates.keys():
        print("-", candidate.title())
    print("\nLet's begin voting! Each voter can vote only once.\n")

def display_candidates():
    """
    Display all available candidates for the election.
    """
    print("Here are the candidates:")
    for candidate in data_manager.candidates.keys():
        print("-", candidate.title())

def display_results():
    """
    Display the current vote tally for all candidates.
    """
    print("\n📊 Current Vote Tally:")
    for candidate, vote_count in data_manager.candidates.items():
        print(f"- {candidate.title()}: {vote_count} votes")

def display_voting_history():
    """
    Display the complete voting record showing which voter voted for which candidate.
    """
    print("\n📝 Voting History:")
    if not data_manager.voting_history:
        print("No votes have been cast yet.")
        return
        
    for voter_name, candidate_choice in data_manager.voting_history.items():
        print(f"- {voter_name.title()} voted for {candidate_choice.title()}")

def display_main_menu():
    """
    Display the main menu options for the election system.
    """
    print("\n🗳️ Election System Main Menu 🗳️")
    print("==============================")
    print("1. Start the Election")
    print("2. Admin Menu (Authentication Required)")
    print("3. View Registered Voters")
    print("4. View Candidates")
    print("5. View Current Election Results (Saves state to file)")
    print("6. Exit")
    
    choice = input("\nEnter your choice (1-6): ")
    return choice

def display_admin_menu():
    """
    Display admin-only menu options.
    """
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
    """
    Display all registered voters and their voting status.
    """
    print("\n📋 Registered Voters List 📋")
    print("==========================")
    
    if not data_manager.voter_credentials:
        print("No voters are registered.")
        return
    
    for voter_name in data_manager.voter_credentials.keys():
        status = "✅ Has voted" if voter_name in data_manager.voting_history else "⏳ Not voted yet"
        print(f"- {voter_name.title()} ({status})")

def view_candidates():
    """
    Display all registered candidates.
    """
    print("\n🏆 Registered Candidates 🏆")
    print("==========================")
    
    if not data_manager.candidates:
        print("No candidates are registered.")
        return
    
    for candidate_name, votes in data_manager.candidates.items():
        print(f"- {candidate_name.title()} (Current votes: {votes})")

def view_current_results():
    """
    Display the current election results without ending the election.
    Shows vote counts, current leader(s), and voting progress.
    """
    print("\n📊 Current Election Results 📊")
    print("===========================")
    
    # Check if any votes have been cast
    if not data_manager.voting_history:
        print("⚠️ No votes have been cast yet.")
        return
    
    # Display vote counts
    display_results()
    
    # Display current leaders
    winning_candidates, highest_vote_count = results.find_winners()
    
    if len(winning_candidates) == 1:
        print(f"\n🥇 Current leader: {winning_candidates[0].title()} with {highest_vote_count} votes")
    else:
        print(f"\n🤝 Currently tied for the lead with {highest_vote_count} votes each:")
        for candidate in winning_candidates:
            print(f"- {candidate.title()}")
    
    # Display voting progress
    total_voters = len(data_manager.voter_credentials)
    votes_cast = len(data_manager.voting_history)
    votes_remaining = len(data_manager.eligible_voters)
    
    if total_voters > 0:
        progress_percentage = (votes_cast / total_voters) * 100
        print(f"\n📈 Voting progress: {votes_cast}/{total_voters} ({progress_percentage:.1f}%)")
        print(f"⏳ Remaining eligible voters: {votes_remaining}")
    
    # Display recent voting activity
    print("\n🔄 Recent voting activity:")
    # Get the last 5 votes (or fewer if there aren't that many)
    recent_votes = list(data_manager.voting_history.items())[-5:]
    for voter, candidate in recent_votes:
        print(f"- {voter.title()} voted for {candidate.title()}")
