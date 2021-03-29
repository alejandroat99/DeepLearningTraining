FROM ubuntu:20.04

RUN apt-get update && apt-get -y update
RUN apt-get install -y python3-pip python3-dev
RUN apt install python3.8
RUN pip3 -q install pip --upgrade

RUN mkdir src
WORKDIR src/
COPY . .

RUN pip3 install -r requirements.txt
RUN pip3 install jupyter notebook

CMD ["jupyter", "notebook", "--port=8888", "--ip=0.0.0.0", "--allow-root"]