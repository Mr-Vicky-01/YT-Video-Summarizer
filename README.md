# YT Video Summarizer
![download](https://github.com/Mr-Vicky-01/YT-Video-Summarizer/assets/143078285/3d9f3e10-193d-4d11-8c4b-e59514c7a350)

## Overview
This project is a YouTube video transcript summarizer that utilizes the YouTube Transcript API and Google's GenerativeAI model (specifically the "gemini-pro" model). It takes a YouTube video URL as input, extracts the transcript from the video, summarizes the content, and provides important points within 250 words.

## Usage
To use the summarizer:
1. Input a YouTube video link.
2. Click on "Get Video Notes" to extract the transcript and generate a summary.
3. The summary will be displayed, providing important points from the video.

## Requirements
- `python3` 
- `youtube_transcript_api`
- `google.generativeai`
- `streamlit`

## Install the dependencies using:
```bash
pip install youtube_transcript_api google.generativeai streamlit
```
## Configuration
Ensure you have a Google API key set up and stored in an environment variable named GOOGLE_API_KEY.

## Project Structure
- yt_video_summarizer.py: Main script containing the summarizer functionality.
- GeminiPro_model: Model directory containing the GenerativeAI model "gemini-pro".

## Running the Project
To run the project:
```bash
streamlit run yt_video_summarizer.py
```

## Demo Video
https://github.com/Mr-Vicky-01/YT-Video-Summarizer/assets/143078285/c488023b-b1fd-43b4-875c-22467ffe0aab

## Link

[Click Here](https://huggingface.co/spaces/Mr-Vicky-01/YT-Summarizer)
