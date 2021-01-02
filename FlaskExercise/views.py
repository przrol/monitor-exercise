from flask import flash, render_template, redirect, request
from FlaskExercise import app


@app.route('/')
def home():
    log = request.values.get('log_button')
    # TODO: Appropriately log the different button presses
    #   with the appropriate log level.
    if log == 'info':
        app.logger.info('Info-Button was clicked!')
    elif log == 'warning':
        app.logger.warning('Warning-Button was clicked!')
    elif log == 'error':
        app.logger.error('Error-Button was clicked!')
    elif log == 'critical':
        app.logger.critical('Critical-Button was clicked!')
    else:
        app.logger.critical('Button unknown!!!')
        
    return render_template(
        'index.html',
        log=log
    )
