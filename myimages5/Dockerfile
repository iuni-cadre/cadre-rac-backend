FROM python:alpine3.8
WORKDIR /usr/local/bin
# Define the ENV variable
ENV PYTHONUNBUFFERED=1
COPY script1.py .
EXPOSE 80
ENTRYPOINT ["python", "-u", "script1.py"]
