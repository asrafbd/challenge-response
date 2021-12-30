# Dockerfile, Challenge C : Output_Problem_B.txt

FROM python:3.9-slim AS stage-0
RUN mkdir -p /opt/python-app
WORKDIR /opt/python-app
COPY ./Problem_A.py .
RUN python ./Problem_A.py

## stage-0 end ##

FROM python:3.9-slim AS stage-1
RUN mkdir -p /opt/python-app
WORKDIR /opt/python-app
COPY ./Problem_B.py .
COPY --from=stage-0 /opt/python-app/Output_Problem_A.txt /opt/python-app 
# Output file location
RUN mkdir -p /data
ENTRYPOINT ["python", "./Problem_B.py"]
