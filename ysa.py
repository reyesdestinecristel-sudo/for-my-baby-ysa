import streamlit as st

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = 1

# Step 1: Ask for name
if st.session_state.step == 1:
    name = st.text_input("Enter your name:")
    if name:
        st.session_state.name = name
        st.session_state.step = 2

# Step 2: Ask for today's date
if st.session_state.step == 2:
    day = st.text_input("What is the date today?")
    if day:
        st.session_state.day = day
        st.session_state.step = 3
        st.write(f"IT'S OUR ANNIV TODAY!! HAPPY ANNIVERSARY, MY {st.session_state.name} i love you so so much, 3yrs na tayo baby (sana naaalala mo pa ha!) let's make more happy memories together okay? at pumunta kung saan saan. Thank u for being there and my kakampi always.")

# Step 3: Where do you want to go
if st.session_state.step == 3:
    st.subheader("Where do you want to go today? Choose a number")
    place_option = st.radio(
        "Pick a number:",
        ["", "1. MOA", "2. Fairview", "3. At your place", "Other"]
    )

    if place_option:
        if place_option == "1. MOA":
            st.write("Yey, let's go! Mag wear tayo ng couple shirt ha ")
        elif place_option == "2. Fairview":
            st.write("Okay baby, let's eat samgy and buy ice cream! ")
        elif place_option == "3. At your place":
            st.write("Nice choice pwede tayo mag kiss hahaha, let's order some foods and watch YOUR BELOVED KHIANNA ")
        else:
            st.write("You want to go there? Then let's go!! Good choice ")

        st.session_state.step = 4  # Move to next step

# Step 4: Fun activity
if st.session_state.step == 4:
    st.subheader("Ano want mo gawin natin? hehehe")
    activity_choice = st.selectbox(
        "Choose an option:",
        ["Select one", "1. Kiss", "2. Hug", "3. Kiss and Hug", "4. Kiss, Hug, and Sex"]
    )

    if activity_choice == "4. Kiss, Hug, and Sex":
        st.write("Yay okayy! Wait for me po. OTW! 🚗💨")
        st.session_state.step = 5  # Move to next step
    elif activity_choice in ["1. Kiss", "2. Hug", "3. Kiss and Hug"]:
        if activity_choice == "1. Kiss":
            st.write("kiss lang? :( Try Again!")
        elif activity_choice == "2. Hug":
            st.write("hug only?!! Try Again!")
        elif activity_choice == "3. Kiss and Hug":
            st.write("kiss and hug lang? parang kulang e. Try again, baby")

# Step 5: Optional message
if st.session_state.step == 5:
    message = st.text_area("Any message for me or wish for us:")
    if message:
        st.write(message)
        st.write("Isend mo sakin yan ha! Hindi ko pa nababasa pero I love you na hehehe ")
        st.write("That's all thank you hahahaha di pa ako marunong mag code ang ikli pa nito pero hirap na hirap na ako, ang hirap naman kasi! I hope maappreciate mo to kahit medyo cringy, Love you ")
