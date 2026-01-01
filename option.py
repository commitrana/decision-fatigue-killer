class Option:
    def __init__(self,name,importance,urgency,effort, time_left):
        self.name = name
        self.importance  = int(importance)
        self.urgency = int(urgency)
        self.effort = int(effort)
        self.time_left = int(time_left)

    def calculate_score(self):
        time_pressure = 5 if self.time_left <= 24 else 0
        return (self.importance + self.urgency + time_pressure) - self.effort

    def explain(self):
        return (
            f"{self.name} scored high because:\n"
            f"- Importance: {self.importance}\n"
            f"- Urgency: {self.urgency}\n"
            f"- Effort: {self.effort}\n"
            f"- Time left: {self.time_left} hours"
        )
