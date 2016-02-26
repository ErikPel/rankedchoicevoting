from copy import copy
import random


class Poll:

    def __init__(self, candidates=None, votes=None):
        if candidates is None:
            self.candidates = {}
        else:
            self.candidates = candidates

        if votes is None:
            self.votes = {}
        else:
            self.votes = votes

    def addVoter(self, name, vote):
        self.votes[name] = vote
        return self.votes[name]

    def addCandidate(self, name, votes=0):
        self.candidates[name] = votes
        return self.candidates[name]

    def getPollResults(self):
        if self.candidates == {}:
            return "You need to add candidates first"
        elif self.votes == {}:
            return "You haven't added any votes"
        votes_counted = self.count_votes(self.candidates, self.votes)
        return votes_counted

    def dict_min_with_random_tie(self, dict):
        min_value = dict[min(dict, key=dict.get)]
        keys_with_smallest_value = []
        for k in dict:
            if dict[k] == min_value:
                keys_with_smallest_value.append(k)
        return random.choice(keys_with_smallest_value)

    def total_number_of_votes(self, results):
        total_number = 0
        for candidate in results:
            total_number += results[candidate]
        return total_number

    def check_if_majority(self, results):
        number_of_votes = self.total_number_of_votes(results)
        half_of_votes = number_of_votes / 2
        #if there are two candidates left with same amount of votes return random one
        if len(results) == 2:
            keys = list(results)
            if results[keys[0]] == results[keys[1]]:
                print("Final two are even in votes, lets flip a coin")
                return random.choice(keys)
        #else just keeps working as usual
        for candidate in results:
            if results[candidate] > half_of_votes:
                return candidate
        return None

    def count_votes(self, candidates, voters):
        candidates_with_values = copy(candidates)
        for voter in voters:
            if len(voters[voter]) > 0:
                first_pick = voters[voter][0]

                if first_pick in candidates_with_values:
                    candidates_with_values[first_pick] += 1

        print("Current voting round results" + str(candidates_with_values))
        majority = self.check_if_majority(candidates_with_values)

        if(majority):
            return majority

        else:
            least_votes = self.dict_min_with_random_tie(candidates_with_values)
            for voter in voters:
                if least_votes in voters[voter]:
                    voters[voter].remove(least_votes)

            candidates.pop(least_votes)
            return self.count_votes(candidates, voters)
