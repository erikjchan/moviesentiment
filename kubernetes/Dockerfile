# Read from Ubuntu Base Image
FROM python:2.7
RUN mkdir -p /service
# Copy over all the files of interest
ADD src /service/src
ADD accessKeys.csv /service/accessKeys.csv
ADD requirements.txt /service/requirements.txt
WORKDIR /service/
RUN pip install -r requirements.txt
CMD python -u src/run.py $APP_SETTINGS
