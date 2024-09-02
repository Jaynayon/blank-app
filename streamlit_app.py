import time
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.mention import mention
from streamlit_extras.badges import badge
from streamlit_extras.stylable_container import stylable_container
from annotated_text import annotated_text
from typing import Literal
import streamlit as st

# Replicate streamlit_extras colored header: add color header feature.
def colored_header(
    label: str = "Nice title",
    description: str = "Cool description",
    color_name: str = "red-70",
    header_color: str = "#31333f"
):
    """
    Shows a header with a colored underline and an optional description.

    Args:
        label (str, optional): Header label. Defaults to "Nice title".
        description (str, optional): Description shown under the header. Defaults to "Cool description".
        color_name (str, optional): Color of the underline. Defaults to "red-70".
    """
    if color_name is None:
        color_name = next(HEADER_COLOR_CYCLE)  # Ensure HEADER_COLOR_CYCLE is defined elsewhere

    st.write(
        f'<h3 style="color: {header_color}; margin-top: 0; margin-bottom: 0;">{label}</h2>',
        unsafe_allow_html=True,
    )
    st.write(
        f'<hr style="background-color: {color(color_name)}; margin-top: 0;'
        ' margin-bottom: 0; height: 3px; border: none; border-radius: 3px;">',
        unsafe_allow_html=True,
    )
    if description:
        st.caption(description)

def color(color_name: str) -> str:
    """Converts a color name to its corresponding CSS color code."""
    color_map = {
        "light-blue-70": "#00c0f2",
        "orange-70": "#ffa421",
        "blue-green-70": "#00d4b1",
        "blue-70": "#1c83e1",
        "violet-70": "#803df5",
        "red-70": "#ff4b4b",
        "green-70": "#21c354",
        "yellow-80": "#faca2b",
    }
    return color_map.get(color_name, "#000000")  # Default to black if color_name is not found

def imageCol():
    # Create 2 columns using Streamlit's built-in layout
    col1, col2 = st.columns(2)
    
    # Add content to the first column
    with col1:
        st.image("./assets/homepage-img.png", use_column_width=True)
    
    # Add content to the second column
    with col2:
        st.image("./assets/logo-transparent-fitted-bottom.png", use_column_width=True)

        subCol1, subCol2, subCol3, subCol4 = st.columns([1, 0.8, 0.6, 1.4])
        with subCol1:
            badge(type="streamlit", url="https://share.streamlit.io/user/jaynayon")
        with subCol2:
            badge(type="twitter", name="nayonjay")
        with subCol3:
            badge(type="github", name="streamlit/streamlit")
        with subCol4:
            mention(
            label="nayon-autobiography",
            icon="github",  # GitHub is also featured!
            url="https://github.com/Jaynayon/nayon-autobiography",
            )
        
        annotated_text(
            ("Strive", "verb", "#8ef"),
            " to find ",
            ("your","adj","#faa"),
            ("voice","noun","#afa"),
            ", and the ",
            ("longer","adj","#faa"),
            " you ",
            ("wait","verb", "#8ef"),
            " to begin, the less ",
            ("likely","adj","#faa"),
            " you are to ",
            ("find","verb", "#8ef"),
            ("it","pronoun", "#fea"),
            " at all."
        )

        with st.spinner('Wait for it...'):
            time.sleep(5)
            # st.toast('Accessing C drive...')
            # time.sleep(.5)
            # st.toast('Deleting System32 folder...')
            # time.sleep(.5)
            # st.toast('Hooray!', icon='🎉')
            # st.snow()
        # sideBar()
        st.success("Done!")

def sideBar():
    with st.sidebar:
        st.image("./assets/logo-transparent-fitted.png", use_column_width=True)
        
        # Handle redirection after the button is clicked
        if st.button('Career'):
            st.write(
                """
                <script>
                window.location.href = '#career';
                </script>
                """,
                unsafe_allow_html=True
            )

def headerExample():
    colored_header(
        label="My New Pretty Colored Header",
        description="This is a description",
        color_name="violet-70",
    )

def stateButton():
# Initialize session state for button label if not already initialized
    if 'reveal_age' not in st.session_state:
        st.session_state.reveal_age = "21"

    # Define the button and handle its press action
    if st.button("Just give me the answer"):
        st.session_state.reveal_age = "Pressed!" if st.session_state.reveal_age == "Reset" else "Reset"

 # Page config
st.set_page_config(
    page_title="Jay Nayon",
    page_icon="./assets/web-icon-white.png",
    layout="wide",
)

# Title/Welcome Container
with st.container():         
    imageCol()

# Autobiography Container
with stylable_container(
        key="container_autobiography",
        css_styles="""
            {
                // background-color: #f2f2f2;
                border-radius: 0.5rem;
                padding: calc(1em - 1px)
            }
            """,
    ):
        with st.container():
            st.title("🤖 My Autobiography")

            aboutMeCol1, aboutMeCol2 = st.columns(2)
            educationCol1, educationCol2 = st.columns(2)
            earlyLifeCol, careerCol = st.columns(2)

            with aboutMeCol1:
                with stylable_container(
                        key="container_black",
                        css_styles="""
                            {
                                background-color: #000;
                                border-radius: 0.5rem;
                                padding: calc(1em - 1px);
                                color: #ffffff;
                            }
                            """,
                    ): 
                        with st.container():
                            # Add a header
                            # st.header("About Me")
                            colored_header(
                                label="About me",
                                description="",
                                color_name="violet-70",
                                header_color="white"
                            )
                            # Display text with a placeholder for the button
                            st.write("""
                            Hello! My name is Jay D. Nayon Jr., and I am 21 years old. 
                            I am currently working as a full time professional learner🧢. 
                            I have a passion for walking, gaslighting (telling myself everything is going to be alright), 
                            and enjoy spending my free time sleeping and thinking about my next meal.
                            """)

                            with st.expander(label="Love of my life"):
                                st.write("My fam, girl, Jesus, bed hahahah")
                            with st.expander(label="Why am I doing this?"):
                                st.write("To compensate with the line graph's font and dimensions")
                            with st.expander(label="Do I have a lot of time?"):
                                st.write("Yes and No, it's just time is fleeting when I enjoy what I'm doing.")

                with aboutMeCol2:
                    with st.container():
                        # Simulate data where "messing around" leads to "finding out"
                        data_points = 20
                        messing_around = np.linspace(0, 10, data_points)
                        finding_out = messing_around ** 2  # A quadratic relationship to indicate more finding out

                        # Create a DataFrame
                        chart_data = pd.DataFrame({
                            "Messing Around": messing_around,
                            "Finding Out": finding_out
                        })

                        # Create the line chart
                        st.line_chart(chart_data.set_index("Messing Around"), height=200, use_container_width=True)

                        # Add titles to the chart
                        st.write("# My life's representation: The More I Mess Around, The More I Find Out😞")
                
            with educationCol1:
                with st.container():
                    # Assuming these coordinates are valid
                    longitude = 123.8693655171926
                    latitude = 10.300895028340864

                    # Create a DataFrame with the coordinate
                    data = pd.DataFrame({
                        'latitude': [latitude],
                        'longitude': [longitude]
                    })

                    st.map(data,zoom=12,use_container_width=True)

            with educationCol2:
                with stylable_container(
                        key="container_black",
                        css_styles="""
                            {
                                background-color: #000;
                                border-radius: 0.5rem;
                                padding: calc(1em - 1px);
                                color: #ffffff;
                            }
                            """,
                    ): 
                        with st.container():
                            # Add a section for education
                            colored_header(
                                label="Education",
                                description="",
                                color_name="orange-70",
                                header_color="white"
                            )

                            st.write("""
                            I completed my elementary education at Tisa I and my high school education at Tisa II. 
                            During high school, I was involved in the Supreme Student Government as a year representative, 
                            served as an occasional emcee, and participated as a professional🧢 back-up dancer and singer, 
                            as well as an amateur journalist and radio broadcaster. And somehow, I still pursued IT.
                            """)

                with stylable_container(
                        key="container_black",
                        css_styles="""
                            {
                                background-color: #000;
                                border-radius: 0.5rem;
                                padding: calc(1em - 1px);
                                color: #ffffff;
                            }
                            """,
                    ): 
                        with st.container():
                            # Add another section
                            colored_header(
                                label="Early Life",
                                description="",
                                color_name="light-blue-70",
                                header_color="white"
                            )

                            st.write("""
                            I was born in Cebu, Philippines, where I grew up and attended school. 
                            My childhood was awesome! I climbed trees, ate rocks, spiders, and 
                            went through rivers in the name of adventure.
                            """)
            
            with earlyLifeCol:
                with stylable_container(
                        key="container_black",
                        css_styles="""
                            {
                                background-color: #000;
                                border-radius: 0.5rem;
                                padding: calc(1em - 1px);
                                color: #ffffff;
                            }
                            """,
                    ): 
                        with st.container():
                             # Add a section for career
                            colored_header(
                                label="Career🧢",
                                description="",
                                color_name="blue-green-70",
                                header_color="white"
                            )

                            st.write("""
                            After graduating High School, I began my career as a professional learner 
                            in Cebu Institute of Technology - University (CIT-U). After classes, I would 
                            simply take off my polo and head to my part-time job at Caltex🧢.
                            """)
            
            with careerCol:
                with st.container():
                    # Custom CSS to adjust the font size
                    st.markdown(
                        """
                        <style>
                        .emoji-container {
                            display: flex;
                            justify-content: center;
                            width: 100%;
                        }
                        .emoji {
                            font-size: 100px; /* Adjust this value to scale the emoji */
                        }
                        </style>
                        """,
                        unsafe_allow_html=True
                    )
                     # Use a container div with a class to apply the centering
                    st.write('<div class="emoji-container"><span class="emoji">🧢🧢🧢</span></div>', unsafe_allow_html=True)
                            

# Portfolio Container
with stylable_container(
        key="container_portfolio",
        css_styles="""
            {
                background-color: #f2f2f2;
                border-radius: 0.5rem;
                padding: calc(1em - 1px)
            }
            """,
    ):
        with st.container():
            st.title("🕶️ My Portfolio")
            
            col1, col2, col3 = st.columns(3)

            with col1:
                 with stylable_container(
                    key="container_white",
                    css_styles="""
                        {
                            background-color: #ffffff;
                            border-radius: 0.5rem;
                            padding: calc(1em - 1px)
                        }
                        """,
                ):
                    with st.container():
                        # Add a section for career
                        colored_header(
                            label="High School",
                            description="Tisa National High School - F.Llamas St., Tisa, Cebu City",
                            color_name="green-70",
                        )
                        st.write("• Awarded as Best Reporter in Sports News")
                        st.write("• District Schools Press Conference (DSPC) Sports radio broadcaster participant")
                        st.write("• 1st Runner-Up, English Month Love Duet")
        
            with col2:
                    with stylable_container(
                        key="container_white",
                        css_styles="""
                            {
                                background-color: #ffffff;
                                border-radius: 0.5rem;
                                padding: calc(1em - 1px)
                            }
                            """,
                    ):
                        with st.container():
                            # Add a section for career
                            colored_header(
                                label="Senior High School",
                                description="Tisa National High School - F.Llamas St., Tisa, Cebu City",
                                color_name="yellow-80",
                            )
                            st.write("• Majored in Computer System Servicing as an ICT student")
                            st.write("• Awarded Mr. Senior High 2019-2020 at Tisa National High School")
                            st.write("• Graduated with High Honors")
                            st.write("• Awarded Best in ICT")
                            st.write("• Awarded in Best in Communications Arts (English)")
                            st.write("• Computer System Servicing NC II Passer")
                            st.write("• Elected as SSG Grade 11 & 12 Representative")

            with col3:
                with stylable_container(
                key="container_white",
                css_styles="""
                    {
                        background-color: #ffffff;
                        border-radius: 0.5rem;
                        padding: calc(1em - 1px);
                    }
                    """,
                ):
                    with st.container():
                        # Add a section for career
                        colored_header(
                            label="College",
                            description="Cebu Institute of Technology - University - Natalio B. Bacalso Ave, Cebu City",
                        )
                        st.write("Team Wildcats - CIT University")
                        st.write("Huawei ICT Competition 2022-2023, Asia-Pacific-Philippines, Network Track Category")
                        st.write("• Successfully advanced to the laboratory exam phase, placing among the top 9 teams ",
                                 "out of 60 participants from leading universities in the Philippines.")
                        st.write("• Team members: Mariel Genodiala, Earl Joseph Claro, Jay Nayon, Jr.")