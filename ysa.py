import streamlit as st

st.title("Happy Anniversary ")

# Ask for name
name = st.text_input("Enter your name:")

if name:
    # Ask for today's date
    day = st.text_input("What is the date today?")

    if day:
        st.write(f"IT'S OUR ANNIV TODAY!! HAPPY ANNIVERSARY, MY {name} ")

        # Where do you want to go
        st.subheader("Where do you want to go today? Choose a number or type where you want to go")
        place_option = st.radio(
            "Pick a number or type where you want to go:",
            ["1. MOA", "2. Fairview", "3. At your place", "Other "]
        )

        if place_option == "1. MOA":
            st.write("Yey, let's go! Mag wear tayo ng couple shirt ha ")
        elif place_option == "2. Fairview":
            st.write("Okay baby, let's eat samgy and buy ice cream! ")
        elif place_option == "3. At your place":
            st.write("Nice choice pwede tayo mag kiss hahaha, let's order some foods and watch YOUR BELOVED KHIANNA ")
        else:
            st.write("You want to go there? Then let's go!! Good choice ")

        # Fun activity loop using selectbox
        st.subheader("Ano want mo gawin natin? hehehe")
        activity_choice = st.selectbox(
            "Choose an option:",
            ["Select one", "1. Kiss", "2. Hug", "3. Kiss and Hug", "4. Your House"]
        )

        if activity_choice == "1. Kiss":
            st.write("kiss lang? :( Try Again!")
        elif activity_choice == "2. Hug":
            st.write("hug only?!! Try Again!")
        elif activity_choice == "3. Kiss and Hug":
            st.write("kiss and hug lang? parang kulang e. Try again, baby")
        elif activity_choice == "4. Your House":
            st.write("Yay okayy! Wait for me po. OTW! 🚗💨")

        # Optional message input
        message = st.text_area("Any message for me or wish for us:")
        if message:
            st.write(message)
            st.write("Isend mo sakin yan ha! Hindi ko pa nababasa pero I love you na hehehe ")
            st.write("That's all thank you hahahaha di pa ako marunong mag code ang ikli pa nito pero hirap na hirap na ako, ang hirap naman kasi! I hope maappreciate mo to kahit medyo cringy, Love you ")
