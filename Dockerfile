
FROM tiangolo/meinheld-gunicorn:python3.7

# Generate requirements from Pipfile and create layer.  Do this early as
# requirements rarely change and can be cached in images (faster builds).
RUN pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY . /flask_template

WORKDIR /flask_template

ENV FLASK_APP app.py

CMD [ "pipenv", "run", "gunicorn", "-w", "4", "-b", ":80", "app:create_app" ]
