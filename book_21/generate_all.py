#!/usr/bin/env python3
import os
import time
from gtts import gTTS

AUDIO_DIR = os.path.join(os.path.dirname(__file__), "audio")
os.makedirs(AUDIO_DIR, exist_ok=True)

print("Starting audio generation for ALC Book 21...")
print("Target Audio Directory:", AUDIO_DIR)

QUIZ_LISTENING_TRANSCRIPTS = {
    "quiz_b": [
        "Number 1. Did everyone contribute food to the company dinner?",
        "Number 2. Will the sudden cold weather have an influence on Sergeant Jones?",
        "Number 3. Who will decide whether the accused man is guilty or innocent?",
        "Number 4. Is Captain Davis going to get his discharge from the service soon?",
        "Number 5. Do you like buying new clothes at the department store?",
        "Number 6. Did Tom's heavy coughing pass the cold to everyone in the room?",
        "Number 7. Do we have plenty of medical supplies for the mission?",
        "Number 8. Is the sergeant urging new students to enlist in the armed forces?",
        "Number 9. What time did the committee bring the long meeting to an end?",
        "Number 10. How much rainfall occurs in the Arizona desert during the summer?",
        "Number 11. Are you the personnel officer in charge of recruiting new workers?",
        "Number 12. Did you inform Captain Miller about the change in the flight plan?",
        "Number 13. Did that traffic accident happen just a couple of hours ago?",
        "Number 14. Is it illegal to drive sixty miles per hour in this school zone?",
        "Number 15. Can fifteen soldiers ride in this small transport vehicle?",
        "Number 16. Do you and your team have specific military duties to carry out today?",
        "Number 17. Do violent sandstorms take place frequently in this dry area?",
        "Number 18. Did the new recruits adapt well to the strict training schedule?",
        "Number 19. Did you ask the commander officially for a three-day pass?",
        "Number 20. Can I submit a photocopy of my official birth certificate?",
        "Number 21. What time do you usually get to the base headquarters on weekdays?",
        "Number 22. Is Mark arriving at the airport on the morning flight?",
        "Number 23. Why did so many recruits fail yesterday's promotion exam?",
        "Number 24. Can you describe the witness who saw the accident?",
        "Number 25. Brand new cars are way too expensive for me. What should I do?"
    ],
    "quiz_a": [
        "Number 1. Did they cancel the soccer match because of the heavy rain?",
        "Number 2. Is this container completely sealed so that air cannot enter?",
        "Number 3. Did the new medicine relieve your headache?",
        "Number 4. Is fifty miles per hour the fastest speed we can drive here?",
        "Number 5. Did the police officer make sure the traffic rules were obeyed?",
        "Number 6. Can I give you a duplicate copy of your contract?",
        "Number 7. Was the judge very strict with the young offender?",
        "Number 8. Did he intentionally drop the fragile glass beaker?",
        "Number 9. Which company made the soap you want to buy?",
        "Number 10. How much liquid can this large glass bottle contain?",
        "Number 11. Is Captain Jackson a member of your family?",
        "Number 12. Did you officially ask for permission to leave early?",
        "Number 13. Did you enjoy the beautiful mountain views in Colorado?",
        "Number 14. Are soldiers allowed to smoke in this ammunition storage area?",
        "Number 15. The swimming pool is filled with dirty water. What must we do?",
        "Number 16. Was the colonel's briefing very long and detailed?",
        "Number 17. Was that heavy snowstorm in the middle of summer normal?",
        "Number 18. Why do you always wear that waterproof raincoat?",
        "Number 19. Was the new exercise program helpful to the trainees?",
        "Number 20. What is inside this sealed metal package?",
        "Number 21. Will the lieutenant tell everyone what tasks they have to perform?",
        "Number 22. Why doesn't Kevin drive his car to work every day?",
        "Number 23. Does Kevin enjoy going fishing more than studying for his test?",
        "Number 24. Can you describe the vehicle that was parked near the hangar?",
        "Number 25. Where can I get a copy of the grammar student textbook?"
    ]
}

total = 0
generated = 0

for quiz_key, text_list in QUIZ_LISTENING_TRANSCRIPTS.items():
    print(f"Processing: {quiz_key}")
    for idx, text in enumerate(text_list, start=1):
        filename = f"{quiz_key}_q{idx}.mp3"
        filepath = os.path.join(AUDIO_DIR, filename)
        total += 1
        if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
            try:
                tts = gTTS(text=text, lang="en", tld="com")
                tts.save(filepath)
                generated += 1
                print(f"  Saved: {filename}")
                time.sleep(0.05)
            except Exception as e:
                print(f"  Error: {filename} -> {e}")
        else:
            print(f"  Existing: {filename}")

print(f"Done! Verified {total} files. Generated {generated} new files.")
