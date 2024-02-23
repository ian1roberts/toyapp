# Use an official Python runtime as a parent image
FROM python:3.12-slim
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/ian1roberts/toyapp.git
RUN pip install -U pip
RUN pip install -U setuptools
RUN cd toyapp
RUN pip install -e ./toyapp/.

# Run toyapp when the container launches
ENTRYPOINT ["toyapp"]
