FROM python:3-alpine
# FROM python:2.7-alpine # for 1.2.0

RUN apk add git g++ 
# g++ required to build Brotli

RUN git clone https://github.com/coreruleset/ftw.git /opt/ftw

WORKDIR /opt/ftw
# RUN git checkout tags/1.2.0 && pip install -r requirements.txt
RUN git checkout master && pip install -r requirements.txt

CMD [/bin/bash] # py.test -s -v test/test_default.py --ruledir=test/yaml
