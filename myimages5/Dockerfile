FROM python:3.7
WORKDIR /usr/local/bin
# Define the ENV variable
ENV PYTHONUNBUFFERED=1
ADD script1.py .
COPY 1.csv .
COPY 2.csv .
EXPOSE 80
ENTRYPOINT ["python", "-u", "script1.py"]
