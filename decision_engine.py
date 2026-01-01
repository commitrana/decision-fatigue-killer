class DecisionEngine:
    def __init__(self):
        self.options = []

    def add_options(self,option):
        self.options.append(option)

    def get_best_option(self):
        max_score = max(opt.calculate_score() for opt in self.options)
        return[opt for opt in self.options if opt.calculate_score() == max_score]
