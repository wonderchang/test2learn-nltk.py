FROM python:3.6.8

WORKDIR /workspace
ADD . /workspace

RUN pip install tox
RUN tox --notest


# vi:et:ts=4:sw=4:cc=80
