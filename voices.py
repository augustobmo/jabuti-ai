from openai import OpenAI

model = OpenAI()

voice = model.audio.speech.create(
    input="Oi! Pode falar!",
    model="tts-1",
    voice="nova",
)

voice.stream_to_file("sounds/detected.mp3")

voice = model.audio.speech.create(
    input="Hmm, deixa eu pensar...",
    model="tts-1",
    voice="nova",
)

voice.stream_to_file("sounds/processing.mp3")