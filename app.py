
import streamlit as st

st.set_page_config(
    page_title="AI Travel Itinerary Planner",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ Personalized Travel Itinerary Planner")
st.write("Create a trip plan based on your destination, budget, interests, and travel group.")

st.success("Free mode enabled — no Gemini API or billing required.")

ACTIVITIES = {
    "Nature": [
        "Explore a scenic viewpoint or nature trail",
        "Visit a garden, lake, or nearby natural attraction",
        "Enjoy a relaxing sunset"
    ],
    "Adventure": [
        "Explore an outdoor activity suitable for the area",
        "Plan a hike or nature walk",
        "Visit a recreation or adventure spot"
    ],
    "Food": [
        "Try local breakfast specialties",
        "Explore local street food",
        "Enjoy a regional dinner"
    ],
    "Culture": [
        "Visit a historical or cultural attraction",
        "Explore local architecture and traditions",
        "Discover local art and handicrafts"
    ],
    "Shopping": [
        "Explore a local market",
        "Shop for souvenirs",
        "Visit a popular shopping area"
    ],
    "Relaxation": [
        "Enjoy a slow and relaxing morning",
        "Spend time at a peaceful location",
        "Keep the evening free to unwind"
    ]
}

with st.form("trip_form"):
    destination = st.text_input("Where do you want to go?", "Manali")
    col1, col2 = st.columns(2)

    with col1:
        days = st.number_input(
            "Trip duration (days)", min_value=1,
            max_value=10, value=3, step=1
        )
        budget = st.number_input(
            "Total budget (₹)", min_value=500,
            value=8000, step=500
        )

    with col2:
        group = st.selectbox(
            "Travelling with",
            ["Solo", "Friends", "Family", "Partner"]
        )
        interests = st.multiselect(
            "Your interests",
            list(ACTIVITIES.keys()),
            default=["Nature", "Food"]
        )

    submitted = st.form_submit_button(
        "Generate My Itinerary",
        type="primary"
    )

if submitted:
    if not destination.strip():
        st.error("Please enter a destination.")
    elif not interests:
        st.error("Please select at least one interest.")
    else:
        daily_budget = budget / days
        itinerary_text = []

        st.header(f"Your {days}-Day Trip to {destination.strip()}")
        st.write(f"**Travel group:** {group}")
        st.write(f"**Total budget:** ₹{budget:,.0f}")
        st.write(f"**Suggested daily budget:** ₹{daily_budget:,.0f}")
        st.caption(
            "Budget is a planning estimate, not a live price quote. "
            "Transport, accommodation, and entry fees may vary."
        )

        for day in range(int(days)):
            first_interest = interests[day % len(interests)]
            second_interest = interests[(day + 1) % len(interests)]

            morning = ACTIVITIES[first_interest][day % 3]
            afternoon = ACTIVITIES[second_interest][(day + 1) % 3]
            evening = "Enjoy local surroundings and plan dinner."

            st.subheader(f"📅 Day {day + 1}")
            st.write(f"🌅 **Morning:** {morning}")
            st.write(f"☀️ **Afternoon:** {afternoon}")
            st.write(f"🌆 **Evening:** {evening}")
            st.write(f"💰 **Budget guide:** ₹{daily_budget:,.0f}")
            st.divider()

            itinerary_text.append(
                f"Day {day + 1} — {destination.strip()}\n"
                f"Morning: {morning}\n"
                f"Afternoon: {afternoon}\n"
                f"Evening: {evening}\n"
                f"Suggested daily budget: ₹{daily_budget:,.0f}\n"
            )

        st.download_button(
            label="⬇️ Download Itinerary",
            data="\n\n".join(itinerary_text),
            file_name="my_travel_itinerary.txt",
            mime="text/plain"
        )
