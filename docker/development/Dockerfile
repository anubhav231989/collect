FROM collect-backend-base:latest

MAINTAINER Anubhav Sidhu <annubhav231989@gmail.com>

RUN apt-get update && \
    apt-get install -y libmysqlclient-dev

ENV XDG_CACHE_HOME=/cache

VOLUME /cache

VOLUME /reports

COPY scripts/tests.sh /usr/local/bin/tests.sh
RUN chmod +x /usr/local/bin/tests.sh

# SET DEFAULT DOCKER CONTAINER ENTRYPOINT AND COMMAND STRING.
ENTRYPOINT [ "tests.sh" ]
CMD ["python3", "manage.py", "test", "--noinput"]

# SOURCE CODE COPYING INTO THE DOCKER CONTAINER IS THE LAST THING
# SINCE TYPICALLY THE APPLICATION SOURCE CODE WILL BE CHANGING SO OFTEN.
# LOWER LAYERS ARE CACHED WHEN THEY DONT CHANGE. BOOSTING PERFORMANCE.
COPY src /application
WORKDIR /application


