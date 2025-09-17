class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        best = 0
        for score in self.scores:
            if score > best:
                best = score
        return best
        # or
        # return max(self.scores)
        # or
        # return self.personal_top_three()[0]

    def personal_top_three(self):
        sorted_scores = sorted(self.scores, reverse = True)
        top_three = sorted_scores[0:3]
        return top_three


