FROM pytorch/pytorch:2.6.0-cuda12.6-cudnn9-runtime

ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /app

# Install Python 3.12 + build dependencies
#RUN apt-get update && apt-get install -y --no-install-recommends git\
#    python3 python3-venv python3-pip python3-dev \
#    && rm -rf /var/lib/apt/lists/*

# Create and activate virtualenv
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Clone ai-toolkit
RUN git clone https://github.com/ostris/ai-toolkit.git /app/ai-toolkit

# Copy application files
COPY . /app

# Set entrypoint
CMD ["python3", "-u", "rp_handler.py"]
