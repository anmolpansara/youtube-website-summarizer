import validators,streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader,UnstructuredURLLoader
import time


## sstreamlit APP
st.set_page_config(page_title="LangChain: Summarize Text From YT or Website", page_icon="🦜")
st.title("🦜 LangChain: Summarize Text From YT or Website")
st.subheader('Summarize URL')

with st.sidebar:
    groq_api_key=st.text_input("Groq API Key",value="",type="password")

generic_url=st.text_input("URL",label_visibility="collapsed")

prompt_template="""
Provide a summary of the following content in 300 words:
Content:{text}
"""

prompt=PromptTemplate(
    input_variables=["text"],
    template=prompt_template
)

if st.button("Summarize the Content from YT or Website"):
     ## Validate all the inputs
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide the information to get started")
    elif not validators.url(generic_url):
        st.error("Please enter a valid Url. It can may be a YT video utl or website url")

    else:
        try:
            with st.spinner("Waiting..."):
                ## loading the website or yt video data
                llm =ChatGroq(model="llama3-8b-8192", api_key=groq_api_key)

                if "youtube.com" in generic_url or "youtu.be" in generic_url:
                    # Add retry logic for YouTube loading
                    max_retries = 2
                    for attempt in range(max_retries):
                        try:
                            loader = YoutubeLoader.from_youtube_url(generic_url, add_video_info=False)
                            docs = loader.load()
                            break
                        except Exception as yt_error:
                            if attempt == max_retries - 1:
                                raise yt_error
                            time.sleep(1)  # Wait before retry
                else:
                    loader=UnstructuredURLLoader(urls=[generic_url],ssl_verify=False,
                                                 headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
                    docs=loader.load()

                if not docs or len(docs) == 0:
                    st.error("No content could be loaded from the URL. Please check if the URL is accessible.")
                else:
                    ## Chain For Summarization
                    chain=load_summarize_chain(llm,chain_type="stuff",prompt=prompt)
                    output_summary=chain.run(docs)

                    st.success(output_summary)
        except Exception as e:
            st.error(f"Error: {str(e)}")
            if "400" in str(e):
                st.error("This might be due to an invalid API key or model. Please check your Groq API key.")
            elif "youtube" in generic_url.lower():
                st.error("YouTube video might be private, age-restricted, or unavailable. Try refreshing or use a different video.")
            else:
                st.error("Please try again or use a different URL.")