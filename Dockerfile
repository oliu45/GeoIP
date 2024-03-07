FROM python:3

COPY GeoIP.py /

RUN pip install requests

ENTRYPOINT ["python3", "/GeoIP.py"]
