#!/bin/bash
/usr/sbin/sshd || echo "fail sshd"
pipenv shell