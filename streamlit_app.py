import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="DocuMind AI",
    page_icon="📚",
)

st.title("📚 DocuMind AI")

tab1, tab2 = st.tabs(["Ask Questions", "Compare Documents"])

# -----------------------------
# ASK TAB
# -----------------------------
with tab1:

    st.header("Ask a Question")

    question = st.text_input(
        "Question",
        placeholder="e.g. What is FastAPI?",
    )

    if st.button("Ask"):

        if question.strip():

            with st.spinner("Thinking..."):

                response = requests.post(
                    f"{API_URL}/ask",
                    json={
                        "question": question,
                    },
                )

            if response.status_code == 200:

                result = response.json()

                st.success("Answer")

                st.write(result["answer"])

                st.divider()

                st.subheader("Sources")

                for citation in result["citations"]:

                    with st.expander(
                        f'{citation["source"]} | Page {citation["page"]}'
                    ):

                        st.write(
                            f'Chunk ID: {citation["chunk_id"]}'
                        )

                        st.write(citation["snippet"])

            else:

                st.error(response.text)

# -----------------------------
# CONTRADICT TAB
# -----------------------------
with tab2:

    st.header("Compare Documents")

    document_1 = st.text_input(
        "Document 1",
        value="fastapi.md",
    )

    document_2 = st.text_input(
        "Document 2",
        value="langchain.md",
    )

    topic = st.text_input(
        "Topic",
        placeholder="e.g. API development",
    )

    if st.button("Compare"):

        with st.spinner("Comparing..."):

            response = requests.post(
                f"{API_URL}/contradict",
                json={
                    "document_1": document_1,
                    "document_2": document_2,
                    "topic": topic,
                },
            )

        if response.status_code == 200:

            result = response.json()

            if result["conflict"]:

                st.error("Conflict Found")

            else:

                st.success("No Conflict")

            st.write(result["reason"])

        else:

            st.error(response.text)