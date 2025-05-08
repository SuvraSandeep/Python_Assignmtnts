# ------------------------------------------
# File Manager Module - Handles file operations for the election system
# ------------------------------------------

import os
import datetime
import data_manager
import results


def save_election_state(file_path="election_state.txt"):
    """
    Save the current state of the election (who has voted, who hasn't, current results)
    This can be called periodically during the election.
    
    Args:
        file_path (str): Path to the file where state should be saved
    """
    try:
        with open(file_path, 'w') as file:
            # Write timestamp
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"Election State as of {timestamp}\n")
            file.write("=" * 50 + "\n\n")
            
            # Write current vote counts
            file.write("Current Vote Counts:\n")
            file.write("-----------------\n")
            for candidate, votes in data_manager.candidates.items():
                file.write(f"{candidate.title()}: {votes} votes\n")
            file.write("\n")
            
            # Write who has voted
            file.write("Voters who have cast their votes:\n")
            file.write("-----------------------------\n")
            if data_manager.voting_history:
                for voter, candidate in data_manager.voting_history.items():
                    file.write(f"{voter.title()} voted for {candidate.title()}\n")
            else:
                file.write("No votes have been cast yet.\n")
            file.write("\n")
            
            # Write who hasn't voted yet
            file.write("Eligible voters who have not yet voted:\n")
            file.write("-----------------------------------\n")
            if data_manager.eligible_voters:
                for voter in data_manager.eligible_voters.keys():
                    file.write(f"{voter.title()}\n")
            else:
                file.write("All registered voters have cast their votes.\n")
            
            file.write("\n" + "=" * 50 + "\n")
            
        print(f"\n✅ Election state saved to {file_path}")
        return True
    except Exception as e:
        print(f"\n❌ Error saving election state: {str(e)}")
        return False

def write_final_results(file_path="results.txt"):
    """
    Write the final election results to a file.
    Should only be called once the election is complete.
    
    Args:
        file_path (str): Path to the file where results should be saved
    
    Returns:
        bool: True if file was successfully written, False otherwise
    """
    try:
        # Get winners information
        winning_candidates, highest_vote_count = results.find_winners()
        
        with open(file_path, 'w') as file:
            # Write header
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"ELECTION FINAL RESULTS - {timestamp}\n")
            file.write("=" * 50 + "\n\n")
            
            # Write summary statistics
            total_voters = len(data_manager.voter_credentials)
            votes_cast = len(data_manager.voting_history)
            
            file.write(f"Total registered voters: {total_voters}\n")
            file.write(f"Total votes cast: {votes_cast}\n")
            participation_rate = (votes_cast / total_voters * 100) if total_voters > 0 else 0
            file.write(f"Voter participation rate: {participation_rate:.1f}%\n\n")
            
            # Write final vote tally
            file.write("FINAL VOTE TALLY\n")
            file.write("-" * 20 + "\n")
            for candidate, vote_count in data_manager.candidates.items():
                file.write(f"{candidate.title()}: {vote_count} votes")
                if vote_count == highest_vote_count and vote_count > 0:
                    file.write(" 🏆")
                file.write("\n")
            file.write("\n")
            
            # Write the winner(s)
            if not data_manager.voting_history:
                file.write("⚠️ No votes were cast in this election.\n")
            elif len(winning_candidates) == 1:
                file.write(f"🏆 WINNER: {winning_candidates[0].title()} with {highest_vote_count} votes\n")
            else:
                file.write(f"🤝 TIE RESULT: The following candidates tied with {highest_vote_count} votes each:\n")
                for candidate in winning_candidates:
                    file.write(f"- {candidate.title()}\n")
            file.write("\n")
            
            # Write complete voting record
            file.write("COMPLETE VOTING RECORD\n")
            file.write("-" * 25 + "\n")
            for voter, candidate in data_manager.voting_history.items():
                file.write(f"{voter.title()} voted for {candidate.title()}\n")
            
            # Write non-voters if any
            if data_manager.eligible_voters:
                file.write("\nVOTERS WHO DID NOT PARTICIPATE\n")
                file.write("-" * 30 + "\n")
                for voter in data_manager.eligible_voters.keys():
                    file.write(f"{voter.title()}\n")
            
            file.write("\n" + "=" * 50 + "\n")
            file.write("End of Election Results")
            
        print(f"\n✅ Final election results saved to {file_path}")
        return True
    except Exception as e:
        print(f"\n❌ Error writing final results: {str(e)}")
        return False
