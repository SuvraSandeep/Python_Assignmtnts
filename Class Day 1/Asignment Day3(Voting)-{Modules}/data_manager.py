# ------------------------------------------
# Data Management Module
# ------------------------------------------

# Global variables for storing application data
voter_credentials = {}
candidates = {}
eligible_voters = {}
voting_history = {}

def initialize():
    """
    Initialize the application's data structures.
    """
    global voter_credentials, candidates, eligible_voters, voting_history
    
    # Initialize the data
    voter_credentials, candidates = initialize_data()
    # Make a copy for tracking who is still eligible to vote
    eligible_voters = voter_credentials.copy()
    # Clear voting history
    voting_history = {}

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

def reset_data():
    """
    Reset all application data to initial state.
    """
    initialize()
    print("✅ All data has been reset to initial state.")