FROM python:3.7-slim-buster
WORKDIR /usr/local/bin

# Install dependencies
RUN apt-get update && apt-get install -y build-essential python3-dev libxml2 libxml2-dev zlib1g-dev
# Define the ENV variable
ENV PYTHONUNBUFFERED=1
COPY line_count.py .
EXPOSE 80
ENTRYPOINT ["python", "-u", "line_count.py"]