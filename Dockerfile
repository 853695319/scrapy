FROM python:3.7

LABEL Name=scrapy Version=0.0.1

WORKDIR /app
COPY ./requirements.txt /app

# Using pipenv:
RUN python3 -m pip install pipenv \
    && pipenv install -r requirments
# CMD ["pipenv", "shell"]
COPY . /app

# SSH service
RUN apt-get update \
    && apt-get install -y openssh-server \
    && mkdir /var/run/sshd /root/.ssh \
    # 通过秘钥登录
    && ./authorized_keys /root/.ssh/authorized_keys \
    # SSH login fix. Otherwise user is kicked off after login
    && sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

# If you’re setting values in the Dockerfile using ENV, you need to push them to a shell initialization file like the /etc/profile example in the Dockerfile above.
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
