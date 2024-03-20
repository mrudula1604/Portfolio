import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie

def homepage(about_gif1, education_gif):
    st.title("Hi, I'm Mrudula")

    # Create a layout with two columns
    col1, col2, col3 = st.columns([0.05, 0.5, 0.4])

    # In the first column, display the About Me text
    with col2:
        st.header("About Me")
        about_me_text = """
            <style>
                    @media screen and (max-width: 600px) {
                        .content {
                            font-size: 14px;
                        }
                    }
                    @media screen and (min-width: 601px) and (max-width: 900px) {
                        .content {
                            font-size: 16px;
                        }
                    }
                    @media screen and (min-width: 901px) {
                        .content {
                            font-size: 18px;
                        }
                    }
            </style>
            <div class = "content">Hello, I'm Mrudula, a graduate student at Northeastern University. I love designing and building web applications. What sets me apart is my belief that software development is not just about coding; it's about creating digital experiences that leave a lasting impact on users. I am dedicated to the craft of product development, always striving to bridge the gap between cutting-edge technology and user needs. I'm driven to create not just websites, but full-fledged digital experiences that captivate and engage users. I believe in the power of technology to transform ideas into tangible products that solve real-world problems. 
            Let's connect and create something incredible together. Thank you!</div>
            """
        st.markdown(about_me_text, unsafe_allow_html=True)
        

    # In the second column, display the image
    
    with col3:
        st_lottie(about_gif1, speed=1)
    
    
    st.markdown("---")
    st.subheader("Education")
    col6, col4, col5 = st.columns([0.05, 0.2, 0.6])
    with col5:
        st.markdown("""
            <style>
                @media screen and (max-width: 600px) {
                    .content {
                        font-size: 14px;
                    }
                }
                @media screen and (min-width: 601px) and (max-width: 900px) {
                    .content {
                        font-size: 16px;
                    }
                }
                @media screen and (min-width: 901px) {
                    .content {
                        font-size: 18px;
                    }
                }
            </style>
            <div class = "content">
                - <strong>Master of Science, Information Systems</strong><br>
                &emsp; - Northeastern University, Boston MA (Expected: December 2024)<br>
                - <strong>Bachelor of Engineering in Electronics and Communication</strong><br>
                &emsp; - Osmania University, Hyderabad, Telangana (June 2022)
            </div>""", 
            unsafe_allow_html=True
        )
    with col4:
        st_lottie(education_gif, speed=1)        
    
    st.markdown("---")
    
    st.subheader("Technical Skills")
    st.markdown("""
        <style>
            @media screen and (max-width: 600px) {
                .table-content {
                    font-size: 14px;
                }
            }
            @media screen and (min-width: 601px) and (max-width: 900px) {
                .table-content {
                    font-size: 16px;
                }
            }
            @media screen and (min-width: 901px) {
                .table-content {
                    font-size: 18px;
                }
            }
        </style>
    """, unsafe_allow_html=True)

    # Data for the table
    data = [
        ["PROGRAMMING LANGUAGES:", "Java, JavaScript, Python, SQL."],
        ["DATABASE:", "MySQL, MongoDB, MS SQL Server, Oracle, PostgreSQL, Redis."],
        ["WEB DEVELOPMENT:", "HTML, CSS, SASS, ES5, Bootstrap, React JS, Node JS, Angular, Axure XP, Figma, Django, Flask Express, Spring Boot."],
        ["TOOLS/IDE:", "Netbeans, VS Code, Eclipse, Jupyter notebook, MySQL Workbench, Git, Power BI."],
        ["OTHER SKILLS:", "Agile/Scrum, Elasticsearch, Jira."],
        ["Certificates:", "Python Data Structures, Google IT Support, Design thinking for Innovation."]
    ]

    data_in_dict = {
        "PROGRAMMING LANGUAGES": "Java, JavaScript, Python, SQL",
        "DATABASE": "MySQL, MongoDB, MS SQL Server, Oracle, PostgreSQL, Redis",
        "WEB DEVELOPMENT": "HTML, CSS, SASS, ES5, Bootstrap, React JS, Node JS, Angular, Axure XP, Figma, Django, Flask Express, Spring Boot",
        "TOOLS/IDE": "Netbeans, VS Code, Eclipse, Jupyter notebook, MySQL Workbench, Git, Power BI",
        "OTHER SKILLS": "Agile/Scrum, Elasticsearch, Jira",
        "CERTIFICATES": "Python Data Structures, Google IT Support, Design thinking for Innovation"
    }

    df = pd.DataFrame.from_dict(data_in_dict, orient="index", columns=['Skills'])
    # Render the table
    #st.table(data)
    st.table(df)