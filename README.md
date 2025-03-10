# whispy
## Audio Transcription with Flask, Celery, and Whisper

This project implements an audio transcription service using Flask, Celery, and OpenAI's Whisper model. The transcription process runs asynchronously in the background using Celery workers, with Redis as the message broker and result backend.


### Work Plan

1. Create a new directory and initialize a Git repository.
2. Set up a Python 3.10 virtual environment and install dependencies.
3. Record or download an audio file to test Whisper's transcription capabilities. [`transcribe.py`](transcribe.py) 
4. Retrieve Flask + Celery sample code and set up a background task system.
5. Launch a Redis server as the Celery message broker.
6. Modify the Flask frontend to allow file uploads and retrieve transcription results asynchronously.
7. Continuously check the transcription status until the final result is displayed.


### Prerequisites

#### Install Dependencies
Ensure your system has the required dependencies installed.

```sh
# Update and install FFmpeg (required for audio processing)
sudo apt update && sudo apt install ffmpeg
```

#### Setup Python Environment

Use Python 3.10, as Whisper does not work well with Python 3.11.

```sh
# Install and set up Python 3.10 using pyenv
pyenv install 3.10.0
pyenv local 3.10.0
```

If using Poetry for dependency management:

```sh
# Initialize Poetry virtual environment
poetry install
```

Activate the virtual environment from VSCode:

```sh
eval $(poetry env activate)
code .
```



### Installing Dependencies

```sh
poetry add flask celery redis openai-whisper
```

### Running Redis
To start a Redis container:

```sh
docker run -d -p 6379:6379 redis
```

### Launch Flask Application 

open [`app.py`](app.py) file:
```sh
python app.py
```

### Running Celery Worker
To start the Celery worker, run:

```sh
celery -A tasks.celery_app worker --loglevel=info
```

### Testing the Transcription
- Visit [http://127.0.0.1:5000](http://127.0.0.1:5000/) and upload an audio file.
- The server returns a task ID.
- Periodically check `/get_result?result_id=<task_id>` for the transcription result.

### Resources
* [Whisper - OpenAI](https://openai.com/index/whisper/)
* [Whisper GitHub Repository](https://github.com/openai/whisper)
* [Flask + Celery Pattern](https://flask.palletsprojects.com/en/2.3.x/patterns/celery/)
* [Flask avec celery](https://flask.palletsprojects.com/en/2.3.x/patterns/celery/)


---

*Copyright Hélène Finot - Formation DevOps 2025*
