# ------------------------------------------
# Results Processing Module
# ------------------------------------------

import data_manager

def get_max_votes():
    """
    Get the maximum number of votes received by any candidate.
    
    Returns:
        int: The highest vote count
    """
    return max(data_manager.candidates.values()) if data_manager.candidates else 0

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
    
    for candidate_name, votes in data_manager.candidates.items():
        if votes == highest_vote_count:
            winning_candidates.append(candidate_name)
            
    return winning_candidates, highest_vote_count

def declare_winner():
    """
    Declare the winner(s) of the election and handle tie scenarios.
    """
    winning_candidates, highest_vote_count = find_winners()
    
    if not data_manager.voting_history:
        print("\n⚠️ No votes were cast in this election.")
        return
    
    # Check if there is a single winner or multiple winners (tie)
    if len(winning_candidates) == 1:
        print(f"\n🏆 Winner of the election is: {winning_candidates[0].title()} with {highest_vote_count} votes!")
    else:
        print("\n🤝 It's a tie between the following candidates:")
        for candidate_name in winning_candidates:
            print(f"- {candidate_name.title()} ({data_manager.candidates[candidate_name]} votes)")