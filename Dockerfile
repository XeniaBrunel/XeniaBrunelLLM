# Use the official Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies
# Make sure you have a requirements.txt file in your folder
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Create a Streamlit configuration directory
RUN mkdir -p ~/.streamlit

# Create the config.toml file to handle proxy and CORS issues
# All comments must be in English
RUN echo "\
[server]\n\
port = 8501\n\
address = '0.0.0.0'\n\
enableCORS = false\n\
enableXsrfProtection = false\n\
" > ~/.streamlit/config.toml

# Expose the port Streamlit runs on
EXPOSE 8501

# Start the application
# Run streamlit using app.py instead of main.py
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.enableCORS=false", "--server.enableXsrfProtection=false"]
