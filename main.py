import streamlit as st

import langchain_helper

st.set_page_config(
    page_title="Restaurant Idea Generator",
    page_icon="🍽️",
    layout="centered",
)

st.title("🍽️ Restaurant Idea Generator")
st.caption("Get a creative restaurant name and menu for any cuisine.")

cuisines = [
    "Indian",
    "Italian",
    "Mexican",
    "Arabic",
    "American",
    "Japanese",
    "Thai",
    "French",
]
cuisine = st.sidebar.selectbox("Pick a cuisine", cuisines)

if st.button("Generate ideas", type="primary"):
    with st.spinner(f"Crafting your {cuisine} restaurant..."):
        try:
            response = langchain_helper.generate_restaurant_name_and_items(cuisine)
            st.success("Done!")
            st.header(response["restaurant_name"])
            st.subheader("Menu items")
            for item in response["menu_items"].split(","):
                item = item.strip()
                if item:
                    st.markdown(f"- {item}")
        except ValueError as e:
            st.error(str(e))
        except Exception as e:
            st.error(f"Something went wrong: {e}")
