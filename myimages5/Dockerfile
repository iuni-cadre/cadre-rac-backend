FROM python:3.7
WORKDIR /usr/local/bin

# Define the ENV variable
ENV PYTHONUNBUFFERED=1
COPY helloworld.py .
EXPOSE 80
ENTRYPOINT ["python", "-u", "helloworld.py"]