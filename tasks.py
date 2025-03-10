import whisper
from config import create_app
from celery import shared_task

# Create Flask app and Celery instancy
flask_app = create_app()
celery_app = flask_app.extensions["celery"]

# Celery shared task to transcript audio
@shared_task(ignore_result=False)
def transcribe_audio(file_path: str) -> str:
    try:
        # Load whisper model 
        model = whisper.load_model("tiny")
        # Execute transcription 
        result = model.transcribe(file_path)
        # Return trancription result as text
        return result["text"]
    except Exception as e:
        return f"Error during transcription: {str(e)}"
