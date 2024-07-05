import streamlit as st
from historical_events import get_historical_events


def main():
    """
    Sets up the Streamlit interface for the Historical Events Viewer application.

    Users can input a specific month and day, and upon clicking the "Show Events" button,
    the application will display historical events that occurred on that date.
    """
    st.title("Historical Events Viewer")

    st.write("Enter a date to retrieve historical events.")
    month = st.number_input("Enter the month (e.g., 7 for July):", min_value=1, max_value=12, step=1)
    day = st.number_input("Enter the day (e.g., 1 for 1st):", min_value=1, max_value=31, step=1)

    if st.button("Show Events"):
        events = get_historical_events(month, day)
        if events:
            st.subheader(f"Historical events on {month}/{day}")
            st.divider()
            for event in events:
                st.write(f"**Year:** {event['year']}")
                st.write(f"**Description:** {event['text']}")
                st.write(f"**Link:** {event['links'][0]['link']}")
                st.divider()
        else:
            st.write("Error fetching data. Please try again.")


if __name__ == "__main__":
    main()