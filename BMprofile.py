import streamlit as st
import BMinfo
import pandas as pd

def about_me_section():
    st.header("About Me")
    st.image(BMinfo.profile_picture, width=200)
    st.write(BMinfo.about_me)
    st.write('---')
about_me_section()

def links_section():
    st.sidebar.header("Links")
    st.sidebar.text("Connect with me on LinkedIn")
    linkedin_link = f'<a href="{BMinfo.my_linkedin_url}"><img src= "{BMinfo.linkedin_image_url}" alt="Linkedin" width="75" height="75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
    st.sidebar.text("Checkout My Work")
    github_link = f'<a href="{BMinfo.my_github_url}"><img src= "{BMinfo.github_image_url}" alt="Github" width="65" height="65"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)
    st.sidebar.text("Or Email Me!")
    email_html = f'<a href="mailto:{BMinfo.my_email_address}"><img src= "{BMinfo.email_image_url}" alt="Email" width="75" height="75"></a>'
    st.sidebar.markdown(email_html, unsafe_allow_html=True)
links_section()

def education_section(education_data):
    st.header("Education")
    st.subheader(f"{education_data['Institution']}")
    st.write(f"**Location:{education_data['Location']}**")
    st.write(f"**Degree:{education_data['Degree']}**")
    st.write(f"**Graduation Date:{education_data['Graduation Date']}**")
    st.write("---")
education_section(BMinfo.education_data)

def experience_section(experiences):
    st.header("Professional Experience")
    for title, (details, images) in experiences.items():
        with st.expander(title):
            cols = st.columns(len(images))
            for col, image in zip(cols, images):
                try:
                    col.image(image, width=200)
                except Exception as e:
                    col.warning(f"Image not found: {image}")
            for bullet in details:
                st.write(bullet)
    st.write("---")
experience_section(BMinfo.experiences)

def project_section(projects_data):
    st.header("Projects")
    for project_name, project_description in projects_data.items():
        expander = st.expander(f"{project_name}")
        expander.write(project_description)
    st.write("---")
project_section(BMinfo.projects_data)

def skills_section(programming_data, spoken_data):
    st.header("Skills")
    st.subheader("Programming Languages")
    for skill, percentage in programming_data.items():
        st.write(f'{skill} {BMinfo.programming_icons.get(skill, "")}')
        st.progress(percentage)
    st.subheader("Spoken Languages")
    for spoken, proficiency in spoken_data.items():
        st.write(f'{spoken} {BMinfo.spoken_icons.get(spoken, "")}: {proficiency}')
    st.write("---")
skills_section(BMinfo.programming_data, BMinfo.spoken_data)

def activities_section(leadership_data, activity_data):
    st.header("Activities")
    tab1, tab2 = st.tabs(["Leadership", "Extracurriculars"])
    with tab1:
        st.subheader("Leadership")
        for title, (details, image) in leadership_data.items():
            expander = st.expander(f"{title}")
            expander.image(image, width=250)
            for bullet in details:
                expander.write(bullet)
    with tab2:  
        st.subheader("Extracurriculars")
        for title, details in activity_data.items():
            expander = st.expander(f"{title}")
            for bullet in details:
                expander.write(bullet)
activities_section(BMinfo.leadership_data, BMinfo.activity_data)
