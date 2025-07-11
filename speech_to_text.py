import speech_recognition as sr


def recognize_from_microphone():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        print("⏳ Recognizing...")

    try:
        text = recognizer.recognize_google(audio)
        print("📝 Transcription:")
        print(text)
    except sr.UnknownValueError:
        print("❌ Could not understand audio.")
    except sr.RequestError as e:
        print(f"❌ API error: {e}")

def recognize_from_file(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        print("📝 Transcription from file:")
        print(text)
    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
    except sr.RequestError as e:
        print(f"❌ API error: {e}")

# === Run either method ===
if __name__ == "__main__":
    print("Choose Mode:\n1 - Microphone\n2 - From File")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        recognize_from_microphone()
    elif choice == "2":
        path = input("Enter path to WAV file: ")
        recognize_from_file(path)
    else:
        print("Invalid choice.")
