# Use an official Python image as a base
FROM python:3.10-slim

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file
# COPY requirements.txt .

# Install the dependencies
# RUN pip install -r requirements.txt

# Expose the port that the application will run on
# It doesn't actually publish the port, but instead works as a documentation
# EXPOSE 8000

# Run the command to start the development server
# CMD format instead of EXEC format
CMD ["tail", "-f", "/dev/null"]
