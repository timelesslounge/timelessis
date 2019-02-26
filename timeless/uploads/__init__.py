"""File Uploads"""
from flask_uploads import UploadSet, IMAGES as IMAGES_, configure_uploads


IMAGES = None


def images(app):
    """
    Creates images upload set.
    :param app: Flask application instance
    :return: Images upload set created
    @todo #205:30min Introduce Flask-Uploads configuration parameters to app config.
     According to Flask-Uploads, there is a need to introduce additional configuration
     parameters to the application config instance. Make sure
     UPLOADS_DEFAULT_URL, UPLOADED_IMAGES_URL values are calculated
     according to the current runtime host/port information and
     also UPLOADS_DEFAULT_DEST and UPLOADED_IMAGES_DEST values
     point to correct static resources path
    """
    # Configure the image uploading via Flask-Uploads
    result = UploadSet('images', IMAGES_)
    app.config['UPLOADS_DEFAULT_DEST']= app.instance_path + '/project/static/img/'
    app.config['UPLOADS_DEFAULT_URL'] = 'http://localhost:5000/static/img/'

    app.config['UPLOADED_IMAGES_DEST'] = app.instance_path + '/project/static/img/'
    app.config['UPLOADED_IMAGES_URL'] = 'http://localhost:5000/static/img/'

    configure_uploads(app, result)
    return result
