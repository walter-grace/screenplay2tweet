# Screenplay to Tweets

This is a Streamlit application that helps you split a screenplay into a series of tweets and save them as a CSV file. The application allows you to upload a screenplay, previews the resulting tweets, and provides a link to download the tweets in CSV format.

## Code Overview

The code consists of several functions:

- `read_screenplay(file)`: This function reads the screenplay from a file, removes excess whitespace and specific text associated with the Fade In screenplay software.

- `split_into_tweets(screenplay)`: This function splits the screenplay text into a series of tweets, each no more than 279 characters long.

- `save_tweets_to_csv(tweets)`: This function takes the list of tweets, formats it into a CSV string, and returns the string.

The `main` function is where the Streamlit application is defined. It creates a file uploader for the screenplay, calls the above functions to process the screenplay and create the tweets, and then displays the tweets and a download link for the CSV file.

## Usage

To use this application:

1. Install the required Python packages: Streamlit (`streamlit`) and base64 (`base64`). You can install them using pip:

   ```bash
   pip install streamlit base64
   ```

2. Run the application:

   ```bash
   streamlit run app.py
   ```

   Replace `app.py` with the name of the Python file that contains the application code.

3. Open the application in your web browser. Streamlit will automatically open a new tab in your default web browser. If not, you can manually navigate to the URL that Streamlit provides in the terminal.

4. Upload your screenplay using the file uploader in the application.

5. Review the tweets that the application generates from your screenplay.

6. Click the "Save Tweets to CSV" button to download a CSV file of the tweets.

## Limitations

This application assumes that the screenplay is a text file. Other file formats are not supported. Furthermore, it assumes that the screenplay uses standard formatting and does not contain any unusual characters or formatting that could cause issues with the tweet splitting or CSV creation.

---