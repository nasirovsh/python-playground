# etl_pipeline.py

from celery import Celery
from celery.schedules import crontab
import pandas as pd
from sqlalchemy import create_engine

# Initialize Celery app
app = Celery('etl_pipeline', broker='redis://localhost:6379')

# Configure Celery
app.conf.update(
    result_backend='redis://localhost:6379',
    task_serializer='json',
    result_serializer='json',
    accept_content=['json'],
    timezone='UTC',
    enable_utc=True,
)

# Configure the Celery beat schedule
app.conf.beat_schedule = {
    'run-etl-every-day-at-1am': {
        'task': 'etl_pipeline.etl_pipeline',
        'schedule': crontab(hour=1, minute=0),
        'args': ('path/to/your/source/file.csv', 'postgresql://username:password@localhost:5432/your_database'),
    },
    'run-etl-every-monday': {
        'task': 'etl_pipeline.etl_pipeline',
        'schedule': crontab(day_of_week=1, hour=3, minute=0),
        'args': ('path/to/your/weekly/source/file.csv', 'postgresql://username:password@localhost:5432/your_database'),
    },
}

# Extract task
@app.task
def extract_data(source):
    # Implement your extraction logic here
    # This could be reading from a file, API, or database
    data = pd.read_csv(source)
    return data.to_dict()

# Transform task
@app.task
def transform_data(data):
    # Implement your transformation logic here
    df = pd.DataFrame(data)
    # Example transformation: capitalizing a column
    df['name'] = df['name'].str.upper()
    return df.to_dict()

# Load task
@app.task
def load_data(data, target):
    # Implement your loading logic here
    df = pd.DataFrame(data)
    engine = create_engine(target)
    df.to_sql('transformed_data', engine, if_exists='append', index=False)
    return f"Loaded {len(df)} rows into the database"

# Main ETL pipeline
@app.task
def etl_pipeline(source, target):
    extracted_data = extract_data.delay(source)
    transformed_data = transform_data.delay(extracted_data.get())
    result = load_data.delay(transformed_data.get(), target)
    return result.get()

if __name__ == '__main__':
    app.start()
