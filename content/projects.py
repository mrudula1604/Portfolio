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
    '''resume_path = "Media/Mrudula.resume.pdf"
    if os.path.exists(resume_path):
        st.download_button(
            label="Download Resume",
            data=open(resume_path, "rb").read(),
            file_name="Mrudula_resume.pdf",
            mime="application/pdf"
        )
    else:
        st.error("Resume file not found. Please check the file path.")
    st.markdown("---")  # Horizontal line to separate sections'''

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
        
        st.subheader("Costco Website")
        st.markdown("""
            -  Redesigned the Costco website on Figma to make it more accessible to enhance project strategies for optimal user satisfaction and engagement encompassing User journey mapping, MoSCoW approach and five planes of UX. 
            -  Improvised the membership signup, Search bar, cart experience and checkout process by implementing comprehensive User Experience research methods.
            - Designed a high-fidelity prototype with proper Interactions and Consistency and evaluated use cases to design the workflows.
            -  <a href="https://www.figma.com/design/qsUlDB52LNN92BQfedim8E/Untitled?node-id=1-2&m=dev"> Link</a>
        """, unsafe_allow_html=True)

        st.subheader("Dollar Tree App")
        st.markdown("""
            - Piloted a transformative product design initiative with a cross-functional team to migrate Dollar Tree's e-commerce platform into a user-friendly mobile app, leveraging comprehensive user research methodologies encompassing user personas, empathy maps, storyboarding, affinity mapping, and SWOT analysis.
            - Crafted high-fidelity prototypes, wireframes, and mockups on Figma, adhering to visual design principles such as typography and design patterns, resulting in an optimal and visually captivating user interface.  <a href="https://www.figma.com/design/fNiDDXF0bLh58TvX8v76Ia/Dollar-Tree-App?node-id=0-1&m=dev"> Link</a>
        """, unsafe_allow_html=True)

        st.subheader("Credit Card Fraud Analysis")
        st.markdown("""
            - Engineered a fraud detection system, incorporating Decision Tree, Support Vector Machines, Naïve Bayes and Logistic Regression. Leveraged Python libraries efficient data preprocessing, Exploratory Data Analysis, feature engineering, model training and evaluation.
	- Compared model accuracies in fraud detection analysis and the best model resulted in 99% accuracy ensuring a fine balance between minimizing false positives and false negatives.
- Applied the stacked model to historical credit card transactions, showcasing a substantial 24% reduction in identified fraudulent cases.
 <a href="https://github.com/mrudula1604/FraudAnalysis"> Link</a>
        """, unsafe_allow_html=True)


        
