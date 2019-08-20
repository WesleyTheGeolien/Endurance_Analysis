FROM jupyter/datascience-notebook

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
# CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "app:server"]