import streamlit as st

# Title of the application
st.title("ETI Performance Evaluation Form")

# Header information
operator_id = st.text_input("Operator ID")
date = st.date_input("Date")
trial_number = st.text_input("Trial Number")
reviewer_id = st.text_input("Reviewer ID")

# Section for scoring
st.subheader("Positioning of the Patient")

# 1. Positioning of the Patient's Head
score1 = st.radio(
    "1. Positioning of Patient's Head: Did the operator properly tilt the head into the sniffing position?",
    options=["Yes - Score 1", "No - Score 0"],
    help="Feedback: The angle of neck flexion should be approximately 35 degrees."
)

# 2. Elevation of the Patient's Head
score2 = st.radio(
    "2. Elevation of Patient's Head: Did the operator properly elevate the head?",
    options=["Yes - Score 1", "No - Score -3"],
    help="Feedback: The angle of face extension should be approximately 15 degrees."
)

st.subheader("Insertion of Direct Laryngoscopy Blade")

# 3. Grip of Laryngoscope
score3 = st.radio(
    "3. Grip of Laryngoscope: Did the operator have a proper grip on the laryngoscope?",
    options=["Proper Grip - Score 2", "Improper Grip - Score 0"],
    help="Feedback: The laryngoscope should be held in the left hand high enough to avoid obstructing blade entry."
)

# 4. Method to Open Mouth
score4 = st.radio(
    "4. Method to Open Mouth: Did the operator open the mouth by scissoring their finger and thumb?",
    options=["Yes - Score 2", "No, used another way - Score 2", "Did not adequately open mouth - Score -1"],
    help="Feedback: Use opposing pressure on the teeth with thumb and middle finger."
)

# 5. Location of the Blade While Inserting Into the Mouth
score5 = st.radio(
    "5. Location of the Blade While Inserting Into the Mouth",
    options=[
        "Right side, sweep left - Score 1",
        "Middle, sweep tongue - Score -1",
        "Other - Score -3"
    ],
    help="Feedback: Start at the right side to sweep the tongue to the left."
)

# 6. Blade Insertion with Respect to the Vallecula
score6 = st.radio(
    "6. Blade Insertion with Respect to the Vallecula",
    options=["In Vallecula - Score 0", "Under Vallecula - Score -1"],
    help="Feedback: Pull blade back into the vallecula."
)

# 7. Force Used while Interacting with Vallecula
score7 = st.radio(
    "7. Force Used while Interacting with Vallecula",
    options=["Appropriate Force - Score 1", "Excessive Force - Score -3", "Insufficient Force - Score -1"],
    help="Feedback: Adjust force direction as needed."
)

# 8. Contact with Teeth During Lifting the Blade
score8 = st.radio(
    "8. Contact with Teeth During Lifting the Blade",
    options=["No Contact - Score 1", "Hit Teeth, No Damage - Score -2", "Hit Teeth, Caused Damage - Score -4"],
    help="Feedback: Blade should be lifted at a 45-degree angle away from the operator."
)

# 9. Order of Events for the Insertion of the Laryngoscope
score9 = st.radio(
    "9. Order of Events for the Insertion of the Laryngoscope",
    options=["Correct Order - Score 0", "Incorrect Order - Score -1"],
    help="Feedback: Ensure correct sequence during procedure."
)

st.subheader("Achieving the Optimal Laryngeal View")

# 10. Final Blade Position in the Vallecula When Lifting for Optimal View
score10 = st.radio(
    "10. Final Blade Position in the Vallecula When Lifting for Optimal View",
    options=["Correct Position - Score 1", "Too Shallow - Score 0", "Too Deep - Score -2", "Not in Vallecula - Score -3"],
    help="Feedback: Adjust blade position as necessary."
)

# 11. Blade Position with Respect to the Oropharynx
score11 = st.radio(
    "11. Blade Position with Respect to the Oropharynx",
    options=["Midline - Score 2", "Restarted from Right - Score -2", "Not Midline - Score -7"],
    help="Feedback: Aim for blade to be in midline."
)

# 12. Lift on Laryngoscope for Proper View
score12 = st.radio(
    "12. Lift on Laryngoscope for Proper View",
    options=["Sufficient Lift - Score 1", "Insufficient Lift - Score -1"],
    help="Feedback: Increase lift at a 45-degree angle if necessary."
)

# 13. Quality of the Vocal Cords View
score13 = st.radio(
    "13. Quality of the Vocal Cords View",
    options=["Vocal Cords in View - Score 1", "Vocal Cords Not in View - Score -1"],
    help="Feedback: Ensure view of vocal cords before intubating."
)

# 14. Angle of Lift on First Attempt
score14 = st.radio(
    "14. Angle of Lift on First Attempt",
    options=["Appropriate Angle (45°) - Score 4", "Too Shallow - Score 0", "Backward onto Teeth - Score -2"],
    help="Feedback: Adjust handle to keep angle around 45 degrees."
)

# 15. Multiple Blade Insertion Attempts to Achieve Proper View
score15 = st.radio(
    "15. Multiple Blade Insertion Attempts to Achieve Proper View",
    options=["First Attempt - Score 2", "2-3 Attempts - Score 0", "4+ Attempts - Score -3", "No Proper View - Score -5"],
    help="Feedback: Optimize early attempts for efficiency."
)

st.subheader("Inserting the Endotracheal Tube")

# 16. Number of Contacts of Tube During Insertion
score16 = st.radio(
    "16. Number of Contacts of Tube During Insertion",
    options=["No or Negligible Contact - Score 3", "Excessive Contact - Score -2", "Tube Not Inserted - Score -8"],
    help="Feedback: Minimize contact during insertion."
)

# 17. Multiple Intubation Attempts
score17 = st.radio(
    "17. Multiple Intubation Attempts",
    options=["First Attempt - Score 3", "One Additional Attempt - Score 0", "Two or More Attempts - Score -4", "Intubation Unsuccessful - Score -7"],
    help="Feedback: Ensure clear view of vocal cords before intubating."
)

st.subheader("Avoiding Injury to the Patient")

# 18. Was Excessive Force Used to Insert the Laryngoscope into the Oropharynx?
score18 = st.radio(
    "18. Was Excessive Force Used to Insert the Laryngoscope into the Oropharynx?",
    options=["No - Score 1", "Yes - Score -2"],
    help="Feedback: Reduce approach rate and observe tissues."
)

# 19. Was Excessive Force Used to Insert the ETT into the Oropharynx?
score19 = st.radio(
    "19. Was Excessive Force Used to Insert the ETT into the Oropharynx?",
    options=["No - Score 4", "Yes - Score 1", "Tube Not Inserted - Score -2"],
    help="Feedback: Avoid forcing the ETT into the oropharynx."
)

# 20. Was Excessive Force Used While Interacting with the Vocal Cords?
score20 = st.radio(
    "20. Was Excessive Force Used While Interacting with the Vocal Cords?",
    options=["No - Score 2", "Yes - Score -8"],
    help="Feedback: Use smooth approach to avoid damaging vocal cords."
)

# 21. Laryngoscope Manipulation Around Lip(s)
score21 = st.radio(
    "21. Laryngoscope Manipulation Around Lip(s)",
    options=["No Pinching - Score 0", "Pinched Lips - Score -1"],
    help="Feedback: Ensure lips are clear from laryngoscope blade."
)

# 22. Laryngoscope and ETT Contact with Tissue and Structures
score22 = st.radio(
    "22. Laryngoscope and ETT Contact with Tissue and Structures",
    options=["Appropriate Contact - Score 1", "Excessive Contact - Score 0"],
    help="Feedback: Minimize contact with surrounding tissue."
)

# Submit button
if st.button("Submit"):
    # Calculate total score
    total_score = sum(int(score.split("Score")[-1].strip()) for score in [
        score1, score2, score3, score4, score5, score6, score7, score8,
        score9, score10, score11, score12, score13, score14, score15,
        score16, score17, score18, score19, score20, score21, score22
    ])
    
    st.write("Total Score:", total_score)
    if total_score >= 66:
        st.success("The operator meets the base score requirements.")
    else:
        st.warning("The operator did not meet the base score requirements.")
