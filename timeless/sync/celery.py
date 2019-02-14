from celery import Celery


def make_celery(app):
    print(app.config)
    celery = Celery(
        app.import_name,
        backend=app.config["RESULT_BACKEND"],
        broker=app.config["BROKER_URL"]
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
