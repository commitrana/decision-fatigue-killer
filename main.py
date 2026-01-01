from decision_engine import DecisionEngine
from option import Option

engine = DecisionEngine()



while True:
    print("Add your options")
    name = input("name: ")
    importance = input("importance (1-5): ")
    urgency = input("urgency (1-5): ")
    effort = input("effort (1-5): ")
    time_left = input(("Time it will take: "))

    option = Option(name, importance, urgency, effort, time_left)
    engine.add_options(option)
    more = input("Do you wanna add more options ? yes/no").lower()
    if more == "no":
        break

best_options = engine.get_best_option()
if len(best_options) == 1:
    print(f"\n Best option to do now: {best_options[0].explain()}")
else:
    print(f"it's a tie! choose on of these (preffered the one with high urgency: ) ")
    for opt in best_options:
        print(f" - {opt.name} (score: {opt.calculate_score()}) (urgency: {urgency})")




