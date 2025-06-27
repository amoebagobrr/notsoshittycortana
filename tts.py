from config import ELEVENLABS_API_KEY, ELEVENLABS_MODEL, ELEVENLABS_OUTPUT_FORMAT, ELEVENLABS_VOICE
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play

load_dotenv()

elevenlabs = ElevenLabs(
  api_key=ELEVENLABS_API_KEY,
)


def tts(text):
    audio = elevenlabs.text_to_speech.convert(
    text=text,
    voice_id=ELEVENLABS_VOICE,
    model_id=ELEVENLABS_MODEL,
    output_format=ELEVENLABS_MODEL)
    play(audio)

