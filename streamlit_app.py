import time
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.grid import grid
from streamlit_extras.colored_header import colored_header
from streamlit_extras.mention import mention
from streamlit_extras.badges import badge
from streamlit_extras.stylable_container import stylable_container
from annotated_text import annotated_text

 # Page config
st.set_page_config(
    page_title="Jay Nayon",
    page_icon="./assets/web-icon-white.png",
    layout="wide",
)

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
            "to find ",
            ("your","adj","#faa"),
            ("voice","noun","#afa"),
            ", and the ",
            ("longer","adj","#faa"),
            " you ",
            ("wait","verb", "#8ef"),
            " to begin, the less",
            ("likely","adj","#faa"),
            "you are to ",
            ("find","verb", "#8ef"),
            ("it","pronoun", "#fea"),
            "at all."
        )

        with st.spinner('Wait for it...'):
            time.sleep(5)
            # st.toast('Accessing C drive...')
            # time.sleep(.5)
            # st.toast('Deleting System32 folder...')
            # time.sleep(.5)
            # st.toast('Hooray!', icon='🎉')
            # st.snow()
        st.success("Done!")

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

# st.sidebar.markdown("Hi!")

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
            earlyLifeCol1, earlyLifeCol2 = st.columns(2)
            careerCol1, careerCol2 = st.columns(2)

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
                            )
                            # Display text with a placeholder for the button
                            st.write("""
                            Hello! My name is Jay D. Nayon Jr., and I am 21 years old. 
                            I am currently working as a full time professional learner🧢. 
                            I have a passion for walking, gaslighting (telling myself everything is going to be alright), 
                            and enjoy spending my free time sleeping and thinking about my next meal.
                            """)

                            with st.expander(label="Love of my life"):
                                st.write("My fam, girl, bed hahahah")

                with aboutMeCol2:
                    st.write("test")
                
            with educationCol1:
                st.write("test")

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
                            )

                            st.write("""
                            I completed my elementary education at Tisa I and my high school education at Tisa II. 
                            During high school, I was involved in the Supreme Student Government as a year representative, 
                            served as an occasional emcee, and participated as a professional🧢 back-up dancer and singer, 
                            as well as an amateur journalist and radio broadcaster. And somehow, I still pursued IT.
                            """)
            
            with earlyLifeCol1:
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
                            )

                            st.write("""
                            I was born in Cebu, Philippines, where I grew up and attended school. 
                            My childhood was awesome! I climbed trees, ate rocks, spiders, and 
                            went through rivers in the name of adventure.
                            """)

            with earlyLifeCol2:
                st.write("test")

            with careerCol1:
                st.write("test")
            
            with careerCol2:
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
                                label="Career",
                                description="",
                                color_name="blue-green-70",
                            )

                            st.write("""
                            After graduating High School, I began my career as a professional learner 
                            in Cebu Institute of Technology - University (CIT-U). After classes, I would 
                            simply take off my polo and head to my part-time job at Caltex🧢.
                            """)




# Add a section for hobbies and interests
st.header("Hobbies and Interests")

st.write("""
Outside of work, I enjoy [Your Hobbies/Interests]. 
I believe in maintaining a healthy work-life balance and strive to keep myself engaged in activities that bring me joy.
""")

# Add a section for future goals
st.header("Future Goals")

st.write("""
Looking ahead, I aim to [Your Future Goals]. 
I am motivated to continue growing personally and professionally, and I am eager to see where my journey takes me.
""")

# Footer with contact information
st.header("Contact Information")

st.write("""
Feel free to reach out to me via email at [Your Email Address].
You can also find me on [Your Social Media Links].
""")

def example():
    random_df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

    my_grid = grid(2, [2, 4, 1], 1, 4, vertical_align="bottom")

    # Row 1:
    my_grid.dataframe(random_df, use_container_width=True)
    my_grid.line_chart(random_df, use_container_width=True)
    # Row 2:
    my_grid.selectbox("Select Country", ["Germany", "Italy", "Japan", "USA"])
    my_grid.text_input("Your name")
    my_grid.button("Send", use_container_width=True)
    # Row 3:
    my_grid.text_area("Your message", height=40)
    # Row 4:
    my_grid.button("Example 1", use_container_width=True)
    my_grid.button("Example 2", use_container_width=True)
    my_grid.button("Example 3", use_container_width=True)
    my_grid.button("Example 4", use_container_width=True)
    # Row 5 (uses the spec from row 1):
    with my_grid.expander("Show Filters", expanded=True):
        st.slider("Filter by Age", 0, 100, 50)
        st.slider("Filter by Height", 0.0, 2.0, 1.0)
        st.slider("Filter by Weight", 0.0, 100.0, 50.0)
    my_grid.dataframe(random_df, use_container_width=True)

def example2():
    random_df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

    # Create 2 columns using Streamlit's built-in layout
    col1, col2 = st.columns(2)

    # Add content to the first column
    with col1:
        st.dataframe(random_df, use_container_width=True)
    
    # Add content to the second column
    with col2:
        st.write("""
        Feel free to reach out to me via email at [Your Email Address].
        You can also find me on [Your Social Media Links].
        """)
        st.write("""
        Feel free to reach out to me via email at [Your Email Address].
        You can also find me on [Your Social Media Links].
        """)

# Call the function to render the layout
example2()