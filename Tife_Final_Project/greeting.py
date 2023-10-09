try:
    import pyttsx3

except ModuleNotFoundError:
    print("Please Install the pyttsx3 module to proceed")
    

def greeting_audio(greeting_message):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    
    # Set properties (optional)
    engine.setProperty("rate", 150)  # Speed of speech
    engine.setProperty("volume", 2.0)  # Volume (0.0 to 1.0)

    # Use the text-to-speech engine to convert the greeting to speech
    engine.say(greeting_message)
    engine.runAndWait()

