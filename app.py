from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
import os
import streamlit as st

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")
prompt="""You are Yotube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words. Please provide the summary of the text given here:  """

def predict_result(transcript_text):
    result = model.generate_content(prompt + transcript_text)
    return result.text

def extract_transcript_details(youtube_video_url):
    try:
        video_id=youtube_video_url.split("=")[1]
        
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        st.error(e)
    
st.title("Youtube Video Transcript Summarizer")
video_url = st.text_input("Enter Youtube Video Link: ")

if video_url:
    video_id = video_url.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
    
if st.button("Get Video Notes"):
    transcript_text = extract_transcript_details(video_url)
    
    if transcript_text:
        summary = predict_result(transcript_text=transcript_text)
        st.markdown("## Video Notes:")
        st.write(summary)