# ------------------------------------------
# 🗳️ Election Application — Day 1 Project 🗳️
# ------------------------------------------

# ------------------------------------------
# Dictionary of Voters with their SIGNUMs
# ------------------------------------------
voter_credentials = {
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

# Make a copy for tracking voting progress
eligible_voters = voter_credentials.copy()
voting_history = {}  # Stores who voted for whom

# ------------------------------------------
# Candidate Leaders and Vote Counter
# ------------------------------------------
candidates = {
    "dup": 0,
    "python": 0,
    "java": 0
}

# ------------------------------------------
# Display Welcome Message and Candidates
# ------------------------------------------
print("\n🎉 Welcome to the Ericsson MediationElection 🎉\nCandidates standing for election are:\n")
for candidate in candidates.keys():
    print("-", candidate.title())

print("\nLet's begin voting! Each voter can vote only once.\n")

# ------------------------------------------
# Begin Voting Process
# ------------------------------------------
while eligible_voters:
    voter_name = input('\nEnter your name to cast your vote (or type "END" to stop voting):\n').lower()

    # Handle early termination of voting
    if voter_name == "end":
        confirm = input("\nType 'Y' to end voting and declare results\nOR\nType 'N' to continue voting\n")

        if confirm not in ["Y", "N"]:
            while confirm not in ["Y", "N"]:
                print("⚠️ Invalid input. Please try again.")
                confirm = input("Type 'Y' to end voting or 'N' to continue:\n")
        
        if confirm == "Y":
            break
        elif confirm == "N":
            print("\n✅ Continuing the voting session...\n")
            continue

    # Check if the voter is in the eligible list
    if voter_name in eligible_voters:
        signum = input("Please enter your SIGNUM for authentication:\n").lower()

        if (signum == eligible_voters[voter_name]):
            print("\n✅ Authentication successful! Proceed to vote.\nHere are the candidates:")

            for candidate in candidates.keys():
                print("-", candidate.title())
            
            vote = input("Enter the name of the candidate you wish to vote for:\n").lower()
            confirm_vote = input(f"You chose {vote.title()}. Confirm vote? (Y/N): ").lower()
            if confirm_vote != "y":
                print("Vote cancelled.")
                continue
            if vote in candidates:
                print("\n🎉 Congratulations! Your vote has been cast for", vote.title())
                candidates[vote] += 1
                voting_history[voter_name] = vote
                eligible_voters.pop(voter_name)  # Remove voter to prevent re-voting

                if not eligible_voters:
                    print("🎯 All voters have completed their voting.")
                else:
                    print("\n➡️ Please allow the next voter to proceed.\n")
            else:
                print("❌ Voting failed: Candidate not recognized.")
        else:
            print("🚫 Authentication failed: SIGNUM mismatch. Vote not recorded.")
    
    # Check if voter has already voted
    elif voter_name in voting_history:
        print(f"⚠️ {voter_name.title()}, you have already cast your vote.")
    else:
        print("❌ Your name is not in the voters list.")

# ------------------------------------------
# Voting Session Ends - Time for Results!
# ------------------------------------------
print("\n🔚 Voting session ended. Let's look at the results...\n")

# ------------------------------------------
# Display Results
# ------------------------------------------
max_votes = max(candidates.values())
print("📊 Final Vote Tally:")
for candidate, vote_count in candidates.items():
    print(f"- {candidate.title()}: {vote_count} votes")

# ------------------------------------------
# Declare Winner(s)
# ------------------------------------------
winners = []
for names, votes in candidates.items():
    if (votes == max_votes):
        winners.append(names)

if len(winners) == 1:
    print(f"\n🏆 Winner of the election is: {winners[0].title()} with {max_votes} votes!")
else:
    print("\n🤝 It's a tie between the following candidates:")
    for name in winners:
        print(f"- {name.title()} ({candidates[name]} votes)")

# ------------------------------------------
# Display Voting History
# ------------------------------------------
print("\n📝 Voting History:")
for voter, voted_for in voting_history.items():
    print(f"- {voter.title()} voted for {voted_for.title()}")
