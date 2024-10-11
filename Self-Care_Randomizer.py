import random

self_care_activities = {
    "Happy": [],
    "Sad": [],
    "Boored": [],
    "Stressed": [],
    }

def add_activities():
    print("Let's add some self care activities to your list!")
    for mood in self_care_activities:
        print(f"\nEnter activities that help you when you're feeling {mood}:")
        while True:
            activity = input("Add an activity (or type 'done' to move to the next mood): ")
            if activity.lower() == 'done':
                break
            self_care_activities[mood].append(activity)
        if not self_care_activities[mood]:  # if no activities were added
            print(f"No activities added for {mood}. Moving to the next mood.")

def suggest_activity():
    print("\nHow are you feeling right now? Choose from the following options:")
    print(" - tired\n - stressed\n - happy\n - bored")
    mood = input("Enter your mood: ").lower()

    if mood in self_care_activities and self_care_activities[mood]:
        suggestion = random.choice(self_care_activities[mood])
        print(f"\nYou could try this to feel better: {suggestion}")
    else:
        print("Sorry, no activities available for that mood. Try adding some first.")

add_activities()
suggest_activity()
