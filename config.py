from celery import Celery, Task
from flask import Flask

# Initialization of Celery with Flask app integration for tasks
def celery_init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        # Task on background
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    # Create Celery instancy
    celery_app = Celery(app.name, task_cls=FlaskTask)
    # Load Celery configuration
    celery_app.config_from_object(app.config["CELERY"])
    # Set default Celery instancy
    celery_app.set_default()
    # Use a variable
    app.extensions["celery"] = celery_app
    return celery_app

# Create and configure Flask and Celery
def create_app() -> Flask:
    # Create Flask app
    app = Flask(__name__)
    # Configure Celerey and backend( Redis)
    app.config.from_mapping(
        CELERY=dict(
        broker_url="redis://127.0.0.1:6379/0",  
        result_backend="redis://127.0.0.1:6379/0",
            task_ignore_result=False, # Keep the results to show them !!!
        ),
    )
    # Load additionnals configurations
    app.config.from_prefixed_env()
    celery_init_app(app)
    return app