#!/usr/bin/env python3
# ------------------------------------------
# 🗳️ Enhanced Election Application — Interactive Menu System 🗳️
# ------------------------------------------

import data_manager
import auth
import candidate_manager
import voter_manager
import ui
import voting
import results

def admin_menu_system():
    """
    Admin submenu system that handles all administrative functions.
    """
    # First authenticate as admin
    if not auth.authenticate_admin():
        print("🚫 Access denied. Admin authentication required to access the admin menu.")
        return
    
    while True:
        choice = ui.display_admin_menu()
        
        if choice == "1":
            # Add candidate
            result = candidate_manager.add_candidate()
            print(result)
        elif choice == "2":
            # Remove candidate
            result = candidate_manager.remove_candidate()
            print(result)
        elif choice == "3":
            # Add voter
            result = voter_manager.add_voter()
            print(result)
        elif choice == "4":
            # Remove voter
            result = voter_manager.remove_voter()
            print(result)
        elif choice == "5":
            # Return to main menu
            print("\n🔙 Returning to main menu...")
            break
        else:
            print("\n⚠️ Invalid choice. Please select a number between 1 and 5.")
        
        # Pause before showing the admin menu again
        input("\nPress Enter to continue...")

def run_election():
    """
    Run the main election process from start to finish.
    """
    # Start with welcome message
    ui.display_welcome_message()
    
    # Validate we have voters and candidates before starting
    if not data_manager.voter_credentials:
        print("⚠️ There are no registered voters. Please add voters before starting the election.")
        return
        
    if not data_manager.candidates:
        print("⚠️ There are no registered candidates. Please add candidates before starting the election.")
        return
    
    # Begin the voting loop
    while data_manager.eligible_voters:
        voter_name = input('\nEnter your name to cast your vote (or type "END" to stop voting):\n').lower()

        # Handle early termination command
        if voter_name == "end":
            if voting.handle_early_termination():
                break
            continue
        
        # Process different voter scenarios
        if voting.is_eligible_to_vote(voter_name):
            # Voter is eligible - process their vote
            voting.process_vote(voter_name)
        elif voting.has_already_voted(voter_name):
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
    ui.display_results()
    results.declare_winner()
    ui.display_voting_history()

def menu_system():
    """
    Main menu system that controls the flow of the application.
    """
    print("\n🗳️ Welcome to the Ericsson Mediation Election System 🗳️")
    
    while True:
        choice = ui.display_main_menu()
        
        if choice == "1":
            # Start the election
            run_election()
        elif choice == "2":
            # Enter admin menu
            admin_menu_system()
        elif choice == "3":
            # View registered voters
            ui.view_registered_voters()
        elif choice == "4":
            # View candidates
            ui.view_candidates()
        elif choice == "5":
            # View current election results
            ui.view_current_results()
        elif choice == "6":
            # Exit the system
            print("\n👋 Thank you for using the Election System. Goodbye!")
            break
        else:
            print("\n⚠️ Invalid choice. Please select a number between 1 and 6.")
        
        # Pause before showing the menu again
        input("\nPress Enter to continue...")

# ------------------------------------------
# Start the Election Application
# ------------------------------------------
if __name__ == "__main__":
    # Initialize the data first
    data_manager.initialize()
    # Start the menu system
    menu_system()