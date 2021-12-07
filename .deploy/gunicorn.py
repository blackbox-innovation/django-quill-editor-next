daemon = False
chdir = "/srv/playground"
bind = "0.0.0.0:8000"
workers = 1
threads = 1
timeout = 60
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"
capture_output = True