# Election Application — Day 1 Project

# ----------------------------
# List of voters with their identities
# ----------------------------
voters = {
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

# Creating a backup list to track voters who have already voted
voter_list = voters.copy()
history = {}        #To store the history of voting process.

# ----------------------------
# List of Leaders (Candidates)
# ----------------------------
leaders = {
    "dup": 0,
    "python": 0,
    "java": 0
}

# ----------------------------
# Welcome Message
# ----------------------------
print("\nWelcome to the Ericsson Election\nCandidates standing for election are:\n")
for candidate in leaders.keys():
    print("-", candidate.title())

print("\nLet's begin voting! Each voter can vote only once.\n")

# ----------------------------
# Voting Process
# ----------------------------

while voters:
    voter_name = input('''
"Enter your name below to cast the vote.
Type "END" to stop the Voting process\n''')
    voter_name = voter_name.lower()
    if (voter_name == "end"):
        confirm = input('''Type \'Y\' to end the voting immediately and Declare the RESULTS \n OR \n Type \'N\' to continue the voting\n''')
        if(confirm != "Y" and confirm != "N"):
            while (confirm != "Y" or confirm != "N"):
                print("Unidentified characters\n")
                confirm = input("Type again:\nType \'Y\' to end the voting immediately and Declare the RESULTS \n OR \n Type \'N\' to continue the voting\n")
                if (confirm == "Y" or confirm == "N"):
                    break
                else:
                    continue
        if (confirm == "Y"):
            break
        elif (confirm == "N"):
            print(".........Continueing the Voting session.........")
            continue
    if voter_name in voters.keys():
        signum = input("Write your SIGNUM below to authenticate yourself\n")
        signum = signum.lower()

        if signum in voters[voter_name]:
            print("You are now authenticated and can proceed to cast your vote\nChoose your leader:")

            # Display candidates
            for candidate in leaders.keys():
                print("-", candidate.title())
            vote = input("Type the name of the leader you want to vote for\n")
            vote = vote.lower()

            if vote in leaders:
                print("Congratulations! \n Your vote is casted to", vote.title())
                leaders[vote] = leaders[vote] + 1
                history.update({voter_name:vote})
                voters.pop(voter_name)  # Remove voter after voting
                if voters == {}:
                    print("Everyone on the voters list has completed their voting.")
                else:
                    print("Now, please allow the next person to vote.\n")
            else:
                print("Voting failure: Leader's name mismatch.")
        else:
            print('''Authentication failure: SIGNUM Mismatch.\nYour vote will not be casted.''')
    elif voter_name in history:
        print(voter_name.title(), "you have already casted your vote.")
    else:
        print("Your name is not in the list.")

# ----------------------------
# Election Result
# ----------------------------
print("...............Voting session ended................\n")
max_votes = max(leaders.values())

print("Results:")
for candidate in leaders:
    print(candidate, "got", leaders[candidate], "votes.")

# ----------------------------
# Winner Declaration
# ----------------------------
winners = []
for name, votes in leaders.items():
    if votes == max_votes:
        winners.append(name)

if len(winners) == 1:
    print("\nWinner of the election is:", winners[0].title(), "with", max_votes, "votes.")
else:
    print("\nIt is a tie between the following candidates:")
    for w in winners:
        print(f"- {w.title()} ({leaders[w]} votes)")

for names,choose in history.items():
    print(f'{names} voted to {choose}') 
