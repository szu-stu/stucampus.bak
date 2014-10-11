web: gunicorn -w $WORKER_NUM -b 127.0.0.1:$PORT stucampus.wsgi:application
upload: gunicorn -w $UPLOAD_WORKER_NUM -b 127.0.0.1:$PORT -k gevent stucampus.wsgi:application
