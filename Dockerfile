ARG PORT=443
FROM cypress/browsers:latest

# Install necessary dependencies
RUN apt-get update \
    && apt-get install -y python3 python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set the environment variable for PATH
ENV PATH /home/root/.local/bin:${PATH}

# Expose the specified port
EXPOSE $PORT

CMD uvicorn main:app --host 0.0.0.0 --port $PORT
