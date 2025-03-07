import os
from tasks import flask_app, transcribe_audio 
from celery.result import AsyncResult
from flask import request,jsonify, render_template

@flask_app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@flask_app.route("/trigger_task", methods=["POST"])
def start_task() -> dict[str, object]:
    # Upload audio from form
    audio_file = request.files.get('file')
    if audio_file is None:
        return jsonify({"error": "No audio uploaded"}), 400

    # Save file in /tmp 
    file_path = os.path.join("/tmp", audio_file.filename)
    audio_file.save(file_path)

    # Launch task in the background
    task = transcribe_audio.delay(file_path)
    return jsonify({"result_id": task.id})

@flask_app.get("/get_result")
def task_result() -> dict:
    result_id = request.args.get('result_id')
    if not result_id:
        return jsonify({"error": " 'result_id' parameters required."}), 400

    task = AsyncResult(result_id)
    if task.ready():
        if task.successful():
            return jsonify({
                "ready": task.ready(),
                "successful": task.successful(),
                "value": task.result,
            })
        else:
            return jsonify({'status': 'ERROR', 'error_message': str(task.result)})
    else:
        return jsonify({'status': 'Running'})
    
if __name__ == "__main__":
    flask_app.run(debug=True)