Run your Celery worker as usual:
```shell
celery -A basic_etl_celery worker --loglevel=info
``` 

Run a separate Celery beat process to handle the scheduling:
```shell
celery -A basic_etl_celery beat --loglevel=info
```