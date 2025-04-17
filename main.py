import streamlit as st
from PIL import Image


def load_image(option):
    image_paths = {
        "Product Types": "product_types.png",
        "Payment Methods": "payment_methods.png",
    }
    return Image.open(image_paths.get(option, "default.png"))


def generate_analysis(option):
    analysis_texts = {
        "Product Types": "This visualization shows the distribution of various product types sold. The most popular category is ...",
        "Payment Methods": "This chart represents the different payment methods used by customers. The majority prefer ...",
    }
    return analysis_texts.get(option, "No analysis available.")


# Streamlit UI
st.set_page_config(layout="wide", page_title="Marketing Analysis Dashboard")

# Sidebar with styling
st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {
            background-color: #1f4e79;
            color: white;
            padding: 20px;
        }
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] label {
            color: white;
        }
        .stRadio label {
            font-size: 16px;
            font-weight: bold;
            color: white !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.title("📊 Marketing Analysis")
st.sidebar.markdown("---")
option = st.sidebar.radio(
    "**Select a category:**", ["Product Types", "Payment Methods"]
)

st.title("Marketing Analysis Dashboard")

# Display Visualization
st.image(load_image(option), use_container_width=True)

# Display Analysis
st.subheader("Analysis")
st.write(generate_analysis(option))
