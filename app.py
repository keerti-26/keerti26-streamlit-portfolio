import streamlit as st
import base64

st.set_page_config (
    page_title="Keerti Ojha | Data & AI Engineer",
    page_icon="🚀",
    layout="wide"
)

def set_bg_hack(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.
    The html is set to "cover" so it scales.
    '''
    # set bg name
    main_bg_ext = "jpg"
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack('image1.avif')

# st.title("Keerti Ojha")
st.markdown("<h1 style='color:#7FB8D9;'> Keerti Ojha </h1>", unsafe_allow_html=True)
# st.subheader("Data Engineer building scalable Data Products and AI Native Analytical Solutions")
st.markdown("<h4 style='color:#7FB8D9;'> Data Engineer building scalable Data Products and AI Native Analytical Solutions </h4>", unsafe_allow_html=True)
st.markdown(
    "<p style='color:#7FB8D9;'>📧 <a href='mailto:keertiojha26@gmail.com' style='color:#7FB8D9;'>keertiojha26@gmail.com</a> &nbsp;|&nbsp; "
    "🔗 <a href='https://www.linkedin.com/in/keertiojha/' target='_blank' style='color:#7FB8D9;'>linkedin.com/in/keertiojha</a></p>",
    unsafe_allow_html=True
)

st.divider()

# st.write("Data Engineer with 8+ years of experience specialized in designing end-to-end data architectures, " \
# "high-performance ETL/ELT pipelines, and semantic data layers across marketing, finance, and supply chain domains." \
# " Experienced in developing user-facing data applications and LLM-driven analytics assistants to enable self-service analytics and data-driven decision-making, " \
# "with strong stakeholder collaboration and communication skills.")
st.write(
    "<p style='color:#7FB8D9;'> Data Engineer with 8+ years of experience specialized in designing end-to-end data architectures, " \
"high-performance ETL/ELT pipelines, and semantic data layers across marketing, finance, and supply chain domains." \
" Experienced in developing user-facing data applications and LLM-driven analytics assistants to enable self-service analytics and data-driven decision-making, " \
"with strong stakeholder collaboration and communication skills.</p>",  unsafe_allow_html=True)

st.divider()

st.markdown("<h1 style='color:#7FB8D9;'> Featured Projects </h1>", unsafe_allow_html=True)

projects = {
    "VoiceOps AI Real Time Response Pipeline":{
        "description": "A real-time voice emergency intake pipeline. Callers record audio in the browser, which is transcribed, analyzed by AI, stored as a structured incident in Azure Cosmos DB, and responded to with a synthesized voice reply. A dispatcher dashboard allows filtering and status management of all incidents.",
        "skills": "Azure, FastAPI, Next.js, Cosmos DB, Azure Maps, LLMs",
        "github": "https://github.com/keerti-26/VoiceOps-AI-Real-Time-Emergency-Response-Pipeline"
    },
    "LLM Context Handling LangChain":{
        "description":"This project tackles three key challenges in LLM context handling: delivering clean, relevant context, preventing excessive or repetitive retrieval that wastes tokens, and using a three-layer middleware system to limit the tools passed from MCP to the LLM.",
        "skills" : "Python, LangChain, LLMs, MCP",
        "github": "https://github.com/keerti-26/Agents-using-LangChain"
    },
    "Emergency Calls Pipeline":{
        "description": "The main aim of our project is to handle Emergency audio calls and build a fully functional data pipeline to notify it to the correct entities using various AWS services and demonstrating insights in a reference web application.",
        "skills": "AWS S3, DynamoDB, Lambda, API Gateway, SNS, Streamlit, Pytest, Locust, PowerBI",
        "github": "https://github.com/keerti-26/Emergency-Calls-Data-Pipeline"
    },
    "Deep Research , MCP and Memory Agent using LangChain":{
        "description":"A minimal FastAPI app with LangChain agent endpoints powered by LangGraph, with a lightweight browser frontend",
        "skills": "LLMs, MCP, LangChain, LangGraph, Middleware(Profainty filter)",
        "github": "https://github.com/keerti-26/Langchain-Starter-Repo/tree/master"
    }
}

custom_css = """
<style>
    [data-testid="stExpander"] details {
        background-color: rgba(30, 60, 90, 0.6);
        border: 1px solid #7FB8D9;
        border-radius: 8px;
    }
    [data-testid="stExpander"] details summary {
        color: #7FB8D9;
    }
    [data-testid="stLinkButton"] a,
    [data-testid="stLinkButton"] a:hover,
    [data-testid="stLinkButton"] a:visited {
        color: black !important;
        background-color: white !important;
        border-color: white !important;
    }
    [data-testid="stMarkdown"] details summary {
        color: #7FB8D9;
    }
</style>
"""

st.snow()
st.markdown(custom_css, unsafe_allow_html=True)

for name,details in projects.items():
    with st.expander(name, expanded=True):
        st.write(f"<p style='color:#7FB8D9;'>Description: {details["description"]}</p>",  unsafe_allow_html=True)
        st.write(f"<p style='color:#7FB8D9;'>Skills: {details["skills"]}</p>",  unsafe_allow_html=True)
        st.link_button("Github Link", details["github"])
        # st.markdown("<p style='color:#7FB8D9;'>Project Link: </p>" [Link](https://github.com/keerti-26/VoiceOps-AI-Real-Time-Emergency-Response-Pipeline)", unsafe_allow_html=True)

st.divider()
st.markdown("<h1 style='color:#7FB8D9;'> Certifications </h1>", unsafe_allow_html=True)
certifications=["MIT Applied Generative AI for Digital Transformation", "Azure Data Engineer Associate"]

for i, c in enumerate(certifications, 1):
    st.markdown(f"<p style='color:#7FB8D9;'>{i}. {c}</p>", unsafe_allow_html=True)


