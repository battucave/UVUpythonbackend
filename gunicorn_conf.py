from multiprocessing import cpu_count

# Socket Path
#bind = 'unix:/home/ubuntu/project/Best-of-Logan-backend-main/gunicorn.sock'
bind = "0.0.0.0:8080"

# Worker Options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

# Logging Options
loglevel = 'debug'
accesslog = '/home/ubuntu/project/uvu-main/access_log'
errorlog =  '/home/ubuntu/project/uvu-main/error_log'
