FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /backend

RUN sed -i 's/http:\/\/[a-zA-Z0-9]*.[a-zA-Z0-9]*.*.com/http:\/\/ir.ubuntu.sindad.cloud/g' /etc/apt/sources.list



COPY requirements.txt .

# RUN pip config --user set global.index https://mirror-pypi.runflare.com/simple
# RUN pip config --user set global.index-url https://mirror-pypi.runflare.com/simple
# RUN pip config --user set global.trusted-host mirror-pypi.runflare.com
# RUN pip config --user set global.timeout 60

RUN pip install --upgrade pip
RUN pip install  -r requirements.txt


COPY . .


# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
