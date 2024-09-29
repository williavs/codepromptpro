import streamlit as st
import os
from main import generate_prompt_page

st.set_page_config(layout="wide")

def home_page():
    st.title("Welcome to CodePromptPro")

    st.markdown("""**Build a prompt for your AI-Powered IDE, even if you don't know where to start.**""")

    with st.expander("How It Works", expanded=True):
        st.markdown("""
        1. **Provide Initial Parameters:** Describe your project, its key features, and technical requirements
        2. **Answer Clarifying Questions:** Our AI will ask for additional details to refine the prompt
        3. **Receive Your Comprehensive Prompt:** Get a detailed, AI-generated prompt tailored to your project needs
        """)

    with st.expander("Current Framework Support", expanded=True):
        st.markdown("""
        CodePromptPro is optimized to generate prompts for full-stack web applications with the following technology stack (Framework Agnosticism in Development):
        """)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            ### Frontend
            - **Framework:** React
            - **Language:** TypeScript
            - **Routing:** React Router
            - **State Management:** Context API or Redux
            - **Styling:** CSS Modules or Styled Components
            - **Testing:** Jest and React Testing Library
            """)

            st.markdown("""
            ### Backend
            - **Language:** Python 3.x
            - **Framework:** Flask
            - **ORM:** SQLAlchemy
            - **Serialization:** Marshmallow
            - **Testing:** Pytest
            """)

        with col2:
            st.markdown("""
            ### Database
            - **PostgreSQL** (with SQLAlchemy ORM integration)
            """)

            st.markdown("""
            ### DevOps
            - **Containerization:** Docker and Docker Compose
            - **Infrastructure as Code:** Terraform (for Linode deployment)
            - **CI/CD:** GitHub Actions or Jenkins
            - **Local Development:** LocalStack for cloud service simulation
            """)

            st.markdown("""
            ### Additional Tools
            - **Environment Management:** dotenv
            - **Secrets Management:** git-crypt
            - **Code Quality:** ESLint, Prettier (Frontend), Flake8, Black (Backend)
            - **API Documentation:** Swagger/OpenAPI
            """)

    st.markdown("""
    This stack provides a robust foundation for building modern, scalable web applications. Our AI-generated prompts will guide you through setting up this entire ecosystem, from project structure to deployment configurations.
    """)

    st.success("Ready to create your first prompt? Click on 'Generate Prompt' in the sidebar to get started!")

def main():
    def load_css():
        with open("styles.css", "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Call this function at the start of your app
    load_css()

    # Set default page to Home if not set
    if 'page' not in st.session_state:
        st.session_state.page = "Home"

    # Sidebar navigation
    st.sidebar.title("Navigation")
    if st.sidebar.button("Home", key="home", help="Go to Home Page"):
        st.session_state.page = "Home"
    if st.sidebar.button("Generate Prompt", key="generate_prompt", help="Generate a new prompt"):
        st.session_state.page = "Generate Prompt"
    
    # Add Claude API key input in the sidebar
    claude_api_key = st.sidebar.text_input("Enter your Claude API key", type="password")
    if claude_api_key:
        os.environ["ANTHROPIC_API_KEY"] = claude_api_key

    # Main content
    if st.session_state.page == "Home":
        home_page()
    elif st.session_state.page == "Generate Prompt":
        if not claude_api_key:
            st.warning("Please enter your Claude API key in the sidebar to use the Generate Prompt feature.")
        else:
            generate_prompt_page()

if __name__ == "__main__":
    main()