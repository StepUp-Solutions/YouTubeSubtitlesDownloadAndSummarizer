
# YouTube Subtitle Downloader and Summarizer

Free and Full Open Source Summarizer of Youtube (and others) videos using yt-dlp. No API required.

This script allows you to download subtitles from YouTube videos, convert them from VTT to text format, and copy the content into a prompt to enable to use your favorite chat AI to summarize it.

Stop wasting hours watching hours of hours of videos. Get the gist, and ask for follow ups if you deem it relevant.

![bored cat and woman](img/bored.jpg)

## Features

- Downloads YouTube video subtitles.
- Converts and refines subtitles into plain text format.
- Copies the refined text directly to the clipboard with an intro prompt.
- Ready to paste in your favorite chat AI for the summarizing.

## Limitations

- To change for another language, you need to change the language of the subtitles downloaded (search for `'subtitleslangs': ['en']`) and change the prompt in `intro_text`

## Prerequisites

Before you can use this script, make sure you have Python installed on your system (Python 3.7 or newer is recommended). You will also need the following Python packages:
- `yt_dlp`: for downloading video information and subtitles.
- `pyperclip`: for copying text output to the clipboard.

## Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/StepUpSolutions/YouTubeSubtitlesDownloadAndSummarizer
   cd YouTubeSubtitlesDownloadAndSummarizer
   ```

2. **(Optional) Create a Virtual Environment**
- Run `python -m venv .venv` to create a virtual environment.
- **Activate the Virtual Environment:**
  - On **Windows**: Run `.\.venv\Scripts\activate`.
  - On **Linux/Mac**: Run `source .venv/bin/activate`.

3. **Install required Python packages:**
   ```bash
   pip install yt-dlp pyperclip
   ```

4. **(Optional) Create a shortcut**
   - (Windows) Right-click on the script "Send To" -> "Desktop (create shortcut)"

**Done!** No more endless videos to watch.

## Usage

1. **Run the script:**
   ```bash
   summarize.bat (Windows)
   summarize.sh (Linux)
   ```

2. **Enter the YouTube video URL when prompted.**

The script will download the subtitles (if available), refine them (removing duplicate text and timestamp), and save them as a text file in the 'subs/' directory and copy it in your clipboard with an added prompt for summarizing it.


## Output

The output files will be saved in the `subs/` directory located in the root of your project directory. Each subtitle file will be named according to the title of the video.

## License

This project is licensed under the GNU GPL v3 License - see the [LICENSE](LICENSE) file for details.


---

**Note:** This documentation is fully open source, just like the code. Feel free to contribute, improve, or even add more jokes!

**Maintained by @chgayot at StepUp Solutions**
