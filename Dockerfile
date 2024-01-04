# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Clone the Git repository
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/FreakErn/polestar2mqtt.git /app \
    && ls -las . \
    && pip install --no-cache-dir -r requirements.txt \
    && git clone --branch 1.1.1 https://github.com/leeyuentuen/pypolestar.git

CMD ["python", "polestar2mqtt"]
