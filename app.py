import datetime
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Streamlit Components 101", layout="centered")

st.title("Streamlit Components 101")
st.write(
    """
    This app showcases 10 foundational Streamlit components you can recombine to build
    data apps quickly. Interact with each widget to see how values flow through the
    app. Most components mirror common HTML form elements, but Streamlit wires them
    directly into Python variables.
    """
)

with st.sidebar:
    st.header("Toggle UI Themes")
    dark_mode = st.toggle("Dark mode", value=False)
    st.caption(
        "Use the toggle to emulate a settings switch. Streamlit supports custom theming\n"
        "through configuration files; here we just show state handling."
    )

st.subheader("1. Text input")
name = st.text_input("What's your name?", placeholder="Streamlit learner")
if name:
    st.success(f"Hello, {name}! 👋")
else:
    st.info("Enter a name to see a greeting.")

st.subheader("2. Select box")
framework = st.selectbox(
    "Choose your favorite data app framework",
    ["Streamlit", "Dash", "Gradio", "Voila"],
    index=0,
)
st.write("You selected:", framework)

st.subheader("3. Slider")
slider_value = st.slider("Pick a number", min_value=0, max_value=100, value=25)
st.write("Slider value:", slider_value)

st.subheader("4. Checkbox")
agree = st.checkbox("I understand how checkboxes return booleans", value=True)
st.write("Checkbox state:", agree)

st.subheader("5. Radio buttons")
role = st.radio("Select your role", ["Data Scientist", "Engineer", "Analyst"], index=1)
st.write("Role chosen:", role)

st.subheader("6. Date input")
birthday = st.date_input(
    "Pick a memorable date",
    value=datetime.date.today(),
    min_value=datetime.date(2000, 1, 1),
    max_value=datetime.date.today(),
)
st.write("Selected date:", birthday)

st.subheader("7. File uploader")
file = st.file_uploader("Upload a CSV to preview its contents", type=["csv"])
if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.head())
else:
    st.caption("No file uploaded yet. Try a small CSV to see the preview.")

st.subheader("8. Number input")
quantity = st.number_input("How many samples?", min_value=1, max_value=10, value=3, step=1)
st.write(f"We'll process {quantity} samples.")

st.subheader("9. Color picker")
color = st.color_picker("Pick a highlight color", value="#FF4B4B")
st.write("You picked:", color)

st.subheader("10. Form submission")
with st.form("feedback_form"):
    feedback = st.text_area("What would you build with Streamlit?", height=120)
    submit = st.form_submit_button("Send feedback")

if submit:
    st.success("Thanks for your ideas! Streamlit thrives on community projects.")
    st.write("Your idea:", feedback)

st.divider()

st.caption(
    "Tip: Each widget writes its return value to a Python variable. Combine them with"
    " the layout primitives in Streamlit (columns, tabs, expanders) to build rich"
    " interactive tools without writing JavaScript."
)

if dark_mode:
    st.caption("(Imagine a dark theme here — try the toggle in the sidebar!)")
