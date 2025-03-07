import whisper
from config import create_app
from celery import shared_task

# Create Flask app and Celery instancy
flask_app = create_app()
celery_app = flask_app.extensions["celery"]

@shared_task(ignore_result=False)
def transcribe_audio(file_path: str) -> str:
    try:
        model = whisper.load_model("turbo")
        result = model.transcribe(file_path)
        return result["text"]
    except Exception as e:
        return f"Error during transcription: {str(e)}"
