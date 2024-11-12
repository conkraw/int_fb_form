
import streamlit as st

# Title of the application
st.title("ETI Performance Evaluation Form")

# Header information
operator_id = st.text_input("Operator Email")
date = st.date_input("Date")
reviewer_id = st.text_input("Reviewer Email")

# Section for scoring
st.subheader("Positioning of the Patient")

# 1. Positioning of the Patient's Head
score1 = st.radio(
    "1. Positioning of Patient's Head: Did the operator properly tilt the head into the sniffing position?",
    options=["Yes", "No"],
    help="Feedback: The angle of neck flexion should be approximately 35 degrees."
)

# 2. Elevation of the Patient's Head
score2 = st.radio(
    "2. Elevation of Patient's Head: Did the operator properly elevate the head?",
    options=["Yes", "No"],
    help="Feedback: The angle of face extension should be approximately 15 degrees."
)

st.subheader("Insertion of Direct Laryngoscopy Blade")

# 3. Grip of Laryngoscope
score3 = st.radio(
    "3. Grip of Laryngoscope: Did the operator have a proper grip on the laryngoscope?",
    options=["Proper Grip", "Improper Grip"],
    help="Feedback: The laryngoscope should be held in the left hand high enough to avoid obstructing blade entry."
)

# 4. Method to Open Mouth
score4 = st.radio(
    "4. Method to Open Mouth: Did the operator open the mouth by scissoring their finger and thumb?",
    options=["Yes", "No, used another way", "Did not adequately open mouth"],
    help="Feedback: Use opposing pressure on the teeth with thumb and middle finger."
)

# 5. Location of the Blade While Inserting Into the Mouth
score5 = st.radio(
    "5. Location of the Blade While Inserting Into the Mouth",
    options=[
        "Right side, sweep left",
        "Middle, sweep tongue",
        "Other"
    ],
    help="Feedback: Start at the right side to sweep the tongue to the left."
)

# 6. Blade Insertion with Respect to the Vallecula
score6 = st.radio(
    "6. Blade Insertion with Respect to the Vallecula",
    options=["In Vallecula", "Under Vallecula"],
    help="Feedback: Pull blade back into the vallecula."
)

# 7. Force Used while Interacting with Vallecula
score7 = st.radio(
    "7. Force Used while Interacting with Vallecula",
    options=["Appropriate Force", "Excessive Force", "Insufficient Force"],
    help="Feedback: Adjust force direction as needed."
)

# 8. Contact with Teeth During Lifting the Blade
score8 = st.radio(
    "8. Contact with Teeth During Lifting the Blade",
    options=["No Contact", "Hit Teeth, No Damage", "Hit Teeth, Caused Damage"],
    help="Feedback: Blade should be lifted at a 45-degree angle away from the operator."
)

# 9. Order of Events for the Insertion of the Laryngoscope
score9 = st.radio(
    "9. Order of Events for the Insertion of the Laryngoscope",
    options=["Correct Order", "Incorrect Order"],
    help="Feedback: Ensure correct sequence during procedure."
)

st.subheader("Achieving the Optimal Laryngeal View")

# 10. Final Blade Position in the Vallecula When Lifting for Optimal View
score10 = st.radio(
    "10. Final Blade Position in the Vallecula When Lifting for Optimal View",
    options=["Correct Position", "Too Shallow", "Too Deep", "Not in Vallecula"],
    help="Feedback: Adjust blade position as necessary."
)

# 11. Blade Position with Respect to the Oropharynx
score11 = st.radio(
    "11. Blade Position with Respect to the Oropharynx",
    options=["Midline", "Restarted from Right", "Not Midline"],
    help="Feedback: Aim for blade to be in midline."
)

# 12. Lift on Laryngoscope for Proper View
score12 = st.radio(
    "12. Lift on Laryngoscope for Proper View",
    options=["Sufficient Lift", "Insufficient Lift"],
    help="Feedback: Increase lift at a 45-degree angle if necessary."
)

# 13. Quality of the Vocal Cords View
score13 = st.radio(
    "13. Quality of the Vocal Cords View",
    options=["Vocal Cords in View", "Vocal Cords Not in View"],
    help="Feedback: Ensure view of vocal cords before intubating."
)

# 14. Angle of Lift on First Attempt
score14 = st.radio(
    "14. Angle of Lift on First Attempt",
    options=["Appropriate Angle (45°)", "Too Shallow", "Backward onto Teeth"],
    help="Feedback: Adjust handle to keep angle around 45 degrees."
)

# 15. Multiple Blade Insertion Attempts to Achieve Proper View
score15 = st.radio(
    "15. Multiple Blade Insertion Attempts to Achieve Proper View",
    options=["First Attempt", "2-3 Attempts", "4+ Attempts", "No Proper View"],
    help="Feedback: Optimize early attempts for efficiency."
)

st.subheader("Inserting the Endotracheal Tube")

# 16. Number of Contacts of Tube During Insertion
score16 = st.radio(
    "16. Number of Contacts of Tube During Insertion",
    options=["No or Negligible Contact", "Excessive Contact", "Tube Not Inserted"],
    help="Feedback: Minimize contact during insertion."
)

# 17. Multiple Intubation Attempts
score17 = st.radio(
    "17. Multiple Intubation Attempts",
    options=["First Attempt", "One Additional Attempt", "Two or More Attempts", "Intubation Unsuccessful"],
    help="Feedback: Ensure clear view of vocal cords before intubating."
)

st.subheader("Avoiding Injury to the Patient")

# 18. Was Excessive Force Used to Insert the Laryngoscope into the Oropharynx?
score18 = st.radio(
    "18. Was Excessive Force Used to Insert the Laryngoscope into the Oropharynx?",
    options=["No", "Yes"],
    help="Feedback: Reduce approach rate and observe tissues."
)

# 19. Was Excessive Force Used to Insert the ETT into the Oropharynx?
score19 = st.radio(
    "19. Was Excessive Force Used to Insert the ETT into the Oropharynx?",
    options=["No", "Yes", "Tube Not Inserted"],
    help="Feedback: Avoid forcing the ETT into the oropharynx."
)

# 20. Was Excessive Force Used While Interacting with the Vocal Cords?
score20 = st.radio(
    "20. Was Excessive Force Used While Interacting with the Vocal Cords?",
    options=["No", "Yes"],
    help="Feedback: Use smooth approach to avoid damaging vocal cords."
)

# 21. Laryngoscope Manipulation Around Lip(s)
score21 = st.radio(
    "21. Laryngoscope Manipulation Around Lip(s)",
    options=["No Pinching", "Pinched Lips"],
    help="Feedback: Ensure lips are clear from laryngoscope blade."
)

# 22. Laryngoscope and ETT Contact with Tissue and Structures
score22 = st.radio(
    "22. Laryngoscope and ETT Contact with Tissue and Structures",
    options=["Appropriate Contact", "Excessive Contact"],
    help="Feedback: Minimize contact with surrounding tissue."
)

# User input for comments after Question 22
comments22 = st.text_area(
    "Comments on Laryngoscope and ETT Contact with Tissue and Structures",
    "Please enter your comments here...",
    height=150,
    help="Provide feedback or observations regarding the contact of the laryngoscope and ETT with surrounding tissue and structures."
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
