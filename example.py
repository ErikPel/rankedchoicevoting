from rankedchoicevoting import Poll


candidatesA = {"Bob": 0, "Sue": 0, "Bill": 0}

#votes in array sorted by first choice to last choice
votersA = {
    "a": ['Bob', 'Bill', 'Sue'],
    "b": ['Sue', 'Bob', 'Bill'],
    "c": ['Bill', 'Sue', 'Bob'],
    "d": ['Bob', 'Bill', 'Sue'],
    "f": ['Sue', 'Bob', 'Bill']

}
election = Poll(candidatesA,votersA)
election.addCandidate("Joe", 0)
election.addVoter("g",['Joe','Bob'])
print("Winner: " + election.getPollResults())
