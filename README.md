# SPEECH-RECOGNITION-SYSTEM


📄 Speech Recognition System – Project Description (600 words)
As someone completely new to speech recognition and machine learning, I embarked on this project with the goal of building a basic Speech-to-Text system capable of transcribing short audio clips. The idea was inspired by real-world voice assistants like Siri and Google Assistant. Although I had no prior experience in speech processing or AI, I was determined to build something functional and educational. What helped me bridge the gap was access to powerful open-source libraries and platforms like Python, Streamlit, and SpeechRecognition.

🔧 Tools and Libraries Used
To begin, I used Python 3 as my programming language of choice due to its simplicity and the large number of libraries available for audio processing and machine learning. The main library I used was SpeechRecognition, which provides a high-level API for working with various speech engines. It’s beginner-friendly and supports multiple backends including Google Web Speech API and CMU Sphinx.

To capture real-time audio, I used the PyAudio library, which allows Python to access the system’s microphone. For file-based transcription, I used standard .wav audio files.

All the code was written using PyCharm, a beginner-friendly IDE that made debugging easier with its powerful suggestions, clean UI, and integrated terminal. I also created a CLI-based version to handle both microphone input and audio files, giving users flexibility.

🖥️ Platform & Environment
I developed this project on macOS inside a virtual environment using venv to manage dependencies cleanly. I installed the required packages (speechrecognition, pyaudio, etc.) through pip.

When I tried to run the app, I encountered some platform-specific issues—particularly with certificate validation and missing NLTK tokenizer data (punkt)—but after some troubleshooting and help from ChatGPT (which guided me step-by-step), I was able to resolve them.

📚 Learning Resources & Inspirations
I relied on several learning materials to build this project. These included:

Python official documentation

SpeechRecognition GitHub

FreeCodeCamp tutorials on YouTube

Stack Overflow threads for PyAudio errors and NLTK setup

And most importantly, the assistance provided by ChatGPT, which explained error messages clearly and gave copy-paste-ready solutions tailored to my environment

Through this, I learned how to:

Install and manage Python packages

Use microphones in Python

Process and clean .wav files

Handle exceptions like UnknownValueError and API timeouts

Understand how real-time transcription systems work under the hood

⚙️ System Features
The system has two main modes:

Live Microphone Mode – Captures speech through the system microphone and returns real-time transcriptions using Google’s Web Speech API.

File Mode – Accepts a short audio file (preferably .wav) and transcribes its content to text.

The output is printed on the console. The program also gracefully handles errors like unrecognized speech and lack of internet connectivity.

🚀 Future Scope
While the current system depends on an internet connection and Google's API, I plan to make it fully offline by integrating Wav2Vec2 from HuggingFace. Wav2Vec2 is a transformer-based model that can transcribe speech without needing cloud services, which would:

Improve privacy

Enable usage in remote areas

Make the system scalable for large datasets

I also aim to build a Streamlit web interface for non-technical users to drag and drop files and view transcriptions in the browser. Integration with text summarization, translation, or sentiment analysis could also turn it into a mini voice assistant or audio analysis tool.

🎯 Final Thoughts
This project was my first step into the world of voice AI. With just a few lines of Python and open-source libraries, I was able to create a basic system that feels magical—converting my speech to readable text in real time. It was a rewarding experience, and I now feel more confident to explore deeper topics like NLP, deep learning, and human-computer interaction.
