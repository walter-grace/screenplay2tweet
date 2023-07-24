import streamlit as st
import csv
import textwrap
import base64

def read_screenplay(file):
    screenplay = file.read().decode("utf-8").replace("  ", " ")
    while "  " in screenplay:
        screenplay = screenplay.replace("  ", " ")
## Replaces excess text in some screenplay formats I used FADEIN screenplay software
    return screenplay.replace("(Printed with the demonstration version of Fade In)", "")

def split_into_tweets(screenplay):
    return textwrap.wrap(screenplay, 279)

def save_tweets_to_csv(tweets):
    csv_string = "Tweet Number,Tweet\n"
    for i, tweet in enumerate(tweets, start=1):
        csv_string += f"{i},\"{tweet}\"\n"
    return csv_string

def main():
    st.title("Screenplay to Tweets")
    uploaded_file = st.file_uploader("Upload Screenplay", type=['txt'])
    if uploaded_file is not None:
        screenplay = read_screenplay(uploaded_file)
        tweets = split_into_tweets(screenplay)
        st.header("Preview of Tweets")
        for i, tweet in enumerate(tweets, start=1):
            st.write(f"Tweet {i}: {tweet}")
        csv_string = save_tweets_to_csv(tweets)
        b64 = base64.b64encode(csv_string.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="tweets.csv">Save Tweets to CSV</a>'
        st.markdown(href, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
