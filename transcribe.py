import whisper
import warnings

# Ignore  FP16
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

model = whisper.load_model("turbo")
result = model.transcribe("audio/monolog.mp3")
print(result["text"])