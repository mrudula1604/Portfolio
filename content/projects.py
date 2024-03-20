from PIL import Image
import streamlit as st
import os
import streamlit_timeline as timeline
import json

def read_json(json_path):
    with open(json_path, "r") as f:
        data = json.load(f)
    return data

#timeline_data = read_json("content/JSON/timeline.json")

def load_images(image_path):
    img = Image.open(image_path)
    return img

def projects_page():
    # Define the CSS style block for the dark theme
    dark_theme_css = """
        <style>
            .timeline-container {
            background-color: #333; /* Dark background color */
            color: #fff; /* Light text color */
        }

        .timeline-event-content {
            background-color: #444; /* Darker background for event content */
            color: #ddd; /* Slightly lighter text color for better readability */
        }

        .timeline-item {
            border-color: #666; /* Dark border color */
        }
        </style>
    """

    # Render the dark theme CSS style block
    '''st.markdown(dark_theme_css, unsafe_allow_html=True)
    # Download resume
    st.header("Experience")
    timeline.timeline(timeline_data, height=380)'''
    resume_path = "Media/Mrudula.resume.pdf"
    if os.path.exists(resume_path):
        st.download_button(
            label="Download Resume",
            data=open(resume_path, "rb").read(),
            file_name="Mrudula_resume.pdf",
            mime="application/pdf"
        )
    else:
        st.error("Resume file not found. Please check the file path.")
    st.markdown("---")  # Horizontal line to separate sections

    st.header("Projects")
    
    with st.expander("Projects"):
        st.subheader("Food Delivery Website")
        st.markdown("""
            - Developed a React-based food delivery web app with an intuitive UI to increase user engagement and satisfaction.
            - Implemented a Node.js-based RESTful API with MongoDB for secure transactions, scalability, and efficient data management.
            - Improved operational efficiency, increased revenue generation, and enhanced brand perception <a href="https://github.com/mrudula1604/Food-Delivery-App">Link</a>
        """, unsafe_allow_html=True)

        st.subheader("Quotation App")
        st.markdown("""
            - Demonstrated full-stack development capabilities by integrating front-end React-JS applications with a Postgres database backend.
            - Streamlined the quotation process, significantly improving operational efficiency for sales teams.
            - Enhanced the customer experience by providing quick and accurate quotations <a href = "https://drive.google.com/drive/folders/1M5i3cH443fin_HYPaoADLfQwPbfI0x5e?usp=sharing"> Link</a>
        """, unsafe_allow_html=True)

        st.subheader("Live Messaging and Location Sharing")
        st.markdown("""
            - Leveraged React, Redux, Axios, and Socket.io for application development.
            - Ensured efficient state management, asynchronous data handling, and real-time messaging capabilities.
            - Implemented robust error handling and response parsing, enabling seamless communication among travelers <a href="https://github.com/mrudula1604/Live-Messaging-and-Location-Sharing"> Link </a>
        """, unsafe_allow_html=True)

        st.subheader("Health Care Management System")
        st.markdown("""
            - Developed a system to provide administrative support to healthcare facilities using Java Swing.
            - Built to scale accordingly using cross-work functionalities, which could work natively across different modules.
            - Implemented CRUD operations for admins and created work area management for each role under each division <a href="https://github.com/mrudula1604/Health-Care-Management-System"> Link</a>
        """, unsafe_allow_html=True)