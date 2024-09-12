
"""
@author: Charles H. Gayot

Download subtitles for a video (Youtube) and transform it into a prompt to get a summary or other from an LLM.

"""

import os
import re
import yt_dlp
import pyperclip

def download_subtitles(video_url, output_dir):
    """
    Download the auto-generated English subtitles for a given YouTube video.

    Parameters:
        video_url (str): The URL of the YouTube video.
        output_dir (str): The directory where the downloaded subtitle file will be saved.

    Returns:
        tuple: A tuple containing the path to the downloaded subtitle file and the title of the video.
               If no English subtitles are found, returns None for the subtitle file and the video title.
    """
    ydl_opts = {
        'skip_download': True,
        'writeautomaticsub': True,  # Correct option to download auto-generated subtitles
        'subtitleslangs': ['en'],
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        subtitle_files = info.get('requested_subtitles')
        video_title = info.get('title', 'Unknown Title')  # Get the video title or default to 'Unknown Title'
        if subtitle_files and 'en' in subtitle_files:
            subtitle_file = subtitle_files['en']['filepath']
            return subtitle_file, video_title
        return None, video_title



def refine_vtt_to_txt(vtt_file, txt_file, video_title):
    # Include the video title in the introductory text
    intro_text = (f"Below is an automatic transcript where different speakers are not annotated. "
                  f"Your goal is to summarize it knowing it may contain transcript mistakes. "
                  f"Make chapters with the different topics covered, and try to be as lengthy as possible.\n\n"
                  f"Title: {video_title}\n\n")  # Video title is dynamically added here
def refine_vtt_to_txt(vtt_file, txt_file, video_title):
    """
    Refine a VTT file (subtitles) from YouTube and save it as a plain text file.

    Parameters:
        vtt_file (str): The path to the downloaded VTT subtitle file.
        txt_file (str): The path where the refined plain text file will be saved.
        video_title (str): The title of the video corresponding to the subtitles.

    Returns:
        None
    """
    # Include the video title in the introductory text
    intro_text = (f"Below is an automatic transcript where different speakers are not annotated. "
                  f"Your goal is to summarize it knowing it may contain transcript mistakes. "
                  f"Make chapters with the different topics covered, and try to be as lengthy as possible.\n\n"
                  f"Title: {video_title}\n\n")  # Video title is dynamically added here

    
    with open(vtt_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    unique_lines = set()
    with open(txt_file, 'w', encoding='utf-8') as file:
        file.write(intro_text)
        file.write(intro_text)
        for line in lines:
            # Remove VTT metadata, timestamps, and styling tags
            line = re.sub(r'<.*?>', '', line)  # Remove anything within <>
            cleaned_line = line.strip()
            if (not re.match(r'^\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}', cleaned_line) and 
                not cleaned_line.startswith('WEBVTT') and 
                cleaned_line and 
                cleaned_line not in unique_lines):
                file.write(cleaned_line + '\n')
                unique_lines.add(cleaned_line)

def main():
    while True:  # Start of the loop
        video_url = input("Enter the YouTube video URL: ")
        output_dir = 'subs'
        
        # Create the output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Download subtitles
        vtt_file, video_title = download_subtitles(video_url, output_dir)
        
        if vtt_file:
            txt_file = vtt_file.replace('.vtt', '.txt')
            
            # Refine the subtitles and save as txt
            refine_vtt_to_txt(vtt_file, txt_file, video_title)
            
            # Read the text file content
            with open(txt_file, 'r', encoding='utf-8') as file:
                txt_content = file.read()
            
            # Copy the content to the clipboard
            pyperclip.copy(txt_content)
            
            print(f"Processed subtitles for '{video_title}' saved as {txt_file}")
            print("The text has been copied to the clipboard.")
        else:
            print(f"Failed to download subtitles for '{video_title}'.")

        # Ask user if they want to process another video
        response = input("Do you want to process another video? (y/any): ").strip().lower()
        if response != 'y':
            print("Exiting the program.")
            break  # Exit the loop if the user does not want to continue

if __name__ == "__main__":
    main()
