FROM python:3.10.6

WORKDIR /

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 8080

ENV NUM_WORKERS=4

COPY . .

CMD exec hypercorn main:app --bind 0.0.0.0:8080 --workers $NUM_WORKERS --access-logfile - --access-logformat "%(h)s %(l)s \"%(r)s\" %(s)s Origin:\"%({origin}i)s\" X-Forwarded-For:\"%({x-forwarded-for}i)s\""