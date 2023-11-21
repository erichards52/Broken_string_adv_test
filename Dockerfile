FROM python:3.8.12-bullseye

# Make Dockerfile noninteractive
ENV DEBIAN_FRONTEND=noninteractive

#Install necessary components via apt-get
RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    curl \
    unzip \
    groff \
    less \
    coreutils \
    openjdk-11-jre-headless \
    openjdk-17-jre \
    bedtools \
    nano \
    git

RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Nextflow
WORKDIR /usr/local/
RUN curl -s https://get.nextflow.io | bash
RUN mv nextflow /usr/local/bin/

# Install necessary libraries
RUN pip install scikit-learn
RUN pip install pandas
