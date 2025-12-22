import streamlit as st
from dotenv import load_dotenv
import os
from io import BytesIO
from datetime import datetime

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from google.genai.errors import ClientError

# Load environment variables

load_dotenv()
api_key = os.getenv("gemini")
if not api_key:
    st.error("Gemini API key not found.")
    st.stop()

os.environ["GOOGLE_API_KEY"] = api_key

# Streamlit Page Config

st.set_page_config(page_title="AI Mentor Chat", layout="wide")

# ChatGPT-style CSS (LEFT / RIGHT bubbles)

st.markdown("""
<style>
.chat-row {
    display: flex;
    width: 100%;
    margin: 10px 0;
}

.chat-row.user {
    justify-content: flex-end;
}

.chat-row.assistant {
    justify-content: flex-start;
}

.chat-bubble {
    max-width: 60%;
    padding: 12px 16px;
    border-radius: 18px;
    line-height: 1.6;
    font-size: 15px;
    word-wrap: break-word;
}

/* User bubble (RIGHT) */
.chat-bubble.user {
    background-color: #10a37f;
    color: white;
    border-bottom-right-radius: 4px;
}

/* Assistant bubble (LEFT) */
.chat-bubble.assistant {
    background-color: #2f2f2f;
    color: #f5f5f5;
    border-bottom-left-radius: 4px;
}
</style>
""", unsafe_allow_html=True)


# Prevent direct access

if "mentor_subject" not in st.session_state:
    st.warning("Please select a module first.")
    st.stop()

mentor_subject = st.session_state["mentor_subject"]

if "messages" not in st.session_state:
    st.session_state["messages"] = []


# Header + Download Button

left_col, right_col = st.columns([8, 2])

with left_col:
    st.title(f" {mentor_subject} AI Mentor")
    st.markdown(
        f"""
Hello! I’m your personal **{mentor_subject} mentor**   
Ask me anything related to **{mentor_subject}**.
"""
    )

with right_col:
    if st.session_state["messages"]:
        chat_text = ""
        for msg in st.session_state["messages"]:
            role = "User" if msg["role"] == "user" else "Mentor"
            chat_text += f"{role}: {msg['content']}\n\n"

        st.download_button(
            label="📥 Download Chat",
            data=chat_text,
            file_name=f"ai_chatbot_mentor_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain",
            use_container_width=True
        )

st.divider()


# Display Chat History (LEFT / RIGHT)

for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(
            f"""
            <div class="chat-row user">
                <div class="chat-bubble user">
                    {msg["content"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div class="chat-row assistant">
                <div class="chat-bubble assistant">
                    {msg["content"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


# Chat Input
user_input = st.chat_input("Ask your question...")

#Handle User Input

if user_input:

    # Save user message
    st.session_state["messages"].append(
        {"role": "user", "content": user_input}
    )

    # Show user bubble immediately
    st.markdown(
        f"""
        <div class="chat-row user">
            <div class="chat-bubble user">
                {user_input}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Build conversation history (last 6 messages)
    history = ""
    for msg in st.session_state["messages"][-6:]:
        role = "User" if msg["role"] == "user" else "Mentor"
        history += f"{role}: {msg['content']}\n"

   
    # STRICT DOMAIN PROMPT
    system_prompt = f"""
You are a module-specific AI mentor.

Selected Module: {mentor_subject}

STRICT RULE:
If the question is NOT related to "{mentor_subject}", reply ONLY with:
"Sorry, I don’t know about this question. Please ask something related to the selected module."

Rules:
- Answer only within the selected module
- Be clear, structured, and educational
- Do not hallucinate
- Provide examples where applicable
- if the user telling name or somthing about him listen carefully and respond accordingly
- be friendly and supportive
- if the user says bye or whishes to end the session respond politely and end the session

"""

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        temperature=0.3,
        max_output_tokens=200,
        streaming=True
    )

    prompt = PromptTemplate(
        input_variables=["history", "question"],
        template=system_prompt
        + "\n\nConversation:\n{history}"
        + "\n\nUser Question:\n{question}\nMentor:"
    )


    # Stream Assistant Response (LEFT side)

    assistant_placeholder = st.empty()
    partial_response = ""

    try:
        for chunk in llm.stream(
            prompt.format(history=history, question=user_input)
        ):
            if chunk.content:
                partial_response += chunk.content
                assistant_placeholder.markdown(
                    f"""
                    <div class="chat-row assistant">
                        <div class="chat-bubble assistant">
                            {partial_response}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        # Save assistant response
        st.session_state["messages"].append(
            {"role": "assistant", "content": partial_response}
        )

    except ClientError:
        error_msg = "API quota exceeded. Please wait and try again."
        st.session_state["messages"].append(
            {"role": "assistant", "content": error_msg}
        )
        assistant_placeholder.markdown(
            f"""
            <div class="chat-row assistant">
                <div class="chat-bubble assistant">
                    {error_msg}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
