FROM python:3

RUN pip install --no-cache-dir grpcio
RUN pip install --no-cache-dir protobuf


ADD . /

#COPY app /container/
#CMD [ "python", "/app/grpc_client.py" ]
ENTRYPOINT [ "python", "/app/grpc_client.py" ]


