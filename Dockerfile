FROM python:3.8 as python-base
COPY requirements.txt ./
RUN pip install -r requirements.txt

FROM python:3.8-alpine
COPY --from=python-base /root/.cache /root/.cache
COPY --from=python-base requirements.txt .
RUN pip install -r requirements.txt && rm -rf /root/.cache

COPY *.py ./
COPY apis ./apis

EXPOSE 5000
CMD ["python", "app.py"]
