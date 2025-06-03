# YouTube & Website Summarizer

A Streamlit web application that uses LangChain and Groq AI to automatically summarize content from YouTube videos and websites.

## Features

- 📺 **YouTube Video Summarization**: Extract and summarize transcripts from YouTube videos
- 🌐 **Website Content Summarization**: Summarize content from any publicly accessible website
- 🤖 **AI-Powered**: Uses Groq's LLaMA 3 model for intelligent summarization
- ⚡ **Fast Processing**: Quick and efficient content extraction and summarization
- 🎯 **300-word Summaries**: Concise, focused summaries perfect for quick understanding

## Requirements

- Python 3.8+
- Groq API Key (free at [Groq Console](https://console.groq.com/))

## Installation

1. Clone this repository:
```bash
git clone https://github.com/anmolpansara/youtube-website-summarizer.git
cd youtube-website-summarizer
```

2. Install required packages:
```bash
pip install streamlit langchain langchain-groq langchain-community validators youtube-transcript-api unstructured
```

3. Run the application:
```bash
streamlit run app.py
```

## Usage

1. **Get a Groq API Key**: 
   - Visit [Groq Console](https://console.groq.com/)
   - Sign up for a free account
   - Generate an API key

2. **Run the App**:
   - Enter your Groq API key in the sidebar
   - Paste a YouTube URL or website URL
   - Click "Summarize the Content from YT or Website"
   - Get your 300-word summary!

## Supported URLs

- ✅ YouTube videos (`youtube.com`)
- ✅ News websites
- ✅ Blog posts
- ✅ Documentation sites
- ✅ Any publicly accessible web content

## Tech Stack

- **Frontend**: Streamlit
- **AI Framework**: LangChain
- **LLM**: Groq LLaMA 3 (8B parameters)
- **Document Loaders**: YouTube Loader, URL Loader
- **Validation**: URL validators

## Error Handling

The app includes robust error handling for:
- Invalid URLs
- Private/restricted YouTube videos
- Network connectivity issues
- API rate limits
- Missing content
