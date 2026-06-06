def ask_question(question, options):
    print("\n" + question)
    for key, value in options.items():
        print(f"{key}: {value}")
    answer = input("Choose an option: ").lower()
    return answer

#================================================
# SCORE TRACKING
#================================================
score = {
  "gift": 0,
        "experience": 0,
        "big_gift": 0,
        "small_gifts": 0,
        "sentimental": 0,
        "practical": 0,
        "tech": 0,
        "clothes": 0,
        "jewellery": 0,
        "house": 0,
        "adventure": 0,
        "relaxation": 0,
        "music": 0,
        "food": 0,
        "alone": 0,
        "friends": 0,
        "partner": 0,
}

#================================================
# GIFT BRANCH
#================================================

def gift_branch():
    score["gift"] += 1

    # Q1
    answer = ask_question(
        "Would you rather recieve?",
        {
            "a": "One amazing gift 🎁",
            "b": "5 good gifts 🎉 "
        }
    )

    if answer == "a":
        score["big_gift"] += 1
    elif answer == "b":
        score["small_gifts"] += 1

    # Q2
    answer = ask_question(
        "Do you prefer sentimental or practical?",{"a":"Sentimental 💖 ",
        "b":"Practical 🛠️ "}
    )

    if answer == "a":
        score["sentimental"] += 1
    elif answer == "b":
        score["practical"] += 1

    # Q3
    answer = ask_question(
        "What would you like the most?",
        {
            "a": "Tech 💻",
            "b": "Clothes 👕 ",
            "c": "Jewellery 💎",
            "d": "House things 🏠"
        }
    )

    if answer == "a":
        score["tech"] += 1
    elif answer == "b":
        score["clothes"] += 1
    elif answer == "c":
        score["jewellery"] += 1
    elif answer == "d":
        score["house"] += 1

#================================================
# EXPERIENCE BRANCH
#================================================
def experience_branch():
    score["experience"] += 1

    # Q1
    answer = ask_question(
        "What kind of experience sounds the best?",
        {
            "a": "Adventure 🧗",
            "b": "Relaxation 🧖",
            "c": "Food 🍣",
            "d": "Music "
        }
    )

    if answer == "a":
        score["adventure"] += 1
    elif answer == "b":
        score["relaxation"] += 1
    elif answer == "c":
        score["food"] += 1
    elif answer == "d":
        score["music"] += 1

    # Q2
    answer = ask_question(
        "Who would you want to go with?",
        {
            "a": "Alone",
            "b": "Friends",
            "c": "Me"
        }
    )

    if answer == "a":
        score["alone"] += 1
    elif answer == "b":
        score["friends"] += 1
    elif answer == "c":
        score["partner"] += 1


def run_questionnaire():

    # BRANCH ROUTE
    answer = ask_question(
        "Would you prefer a gift or an experience?",
        {"a": "Gift 🎁", "b": "Experience🎟️"}
    )

    if answer == "a":
        gift_branch()

    elif answer == "b":
        experience_branch()

#================================================
# RESULTS
#================================================
def results_gift():
    print("\n*** RESULTS ***")
    print("Preference: Gift")
    if score["big_gift"] > score["small_gifts"]:
        print("Gift style: One larger gift")
    elif score["small_gifts"] > score["big_gift"]:
        print("Gift style: Multiple smaller gifts")

    if score["sentimental"] > score["practical"]:
         print("Motivation: Sentiment")
    elif score["practical"] > score["sentimental"]:
        print("Motivation : Practical")

    gift_categories = ["tech", "clothes", "jewellery", "house"]
    top_gift_category = max(gift_categories, key=lambda x: score[x])
    gift_category_result = top_gift_category.capitalize()
    print(f"Top category: {gift_category_result}")

def results_experience():
    print("\n*** RESULTS ***")
    print("Preference: Experience")

    experience_categories = ["adventure", "relaxation", "food", "music"]
    top_experience_category = max(experience_categories, key=lambda x: score[x])
    experience_category_result = top_experience_category.capitalize()
    print(f"Type of experience: {experience_category_result}")

    person_selection = ["alone", "friends", "partner"]
    top_person_selection = max(person_selection, key=lambda x: score[x])
    person_selection_result = top_person_selection.capitalize()
    print(f"Who with: {person_selection_result}")


def results():
    if score["gift"] > score["experience"]:
        results_gift()
    elif score["experience"] > score["gift"]:
        results_experience()


if __name__ == "__main__":
    run_questionnaire()
    results()