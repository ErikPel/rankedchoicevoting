# rankedchoicevoting
Python code for doing instant runoff voting polls
Did this for another project but it didn't end up being needed. Maybe someone can get something useful done with it.

#Usage example:

```python
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

```
