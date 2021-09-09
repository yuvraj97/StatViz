FROM ubuntu

ARG CACHEBUST=19

ENV LC_ALL C.UTF-8

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get clean \
 && apt-get update --fix-missing \
 && apt-get install -y \
    python3 \
    python3-pip

WORKDIR /work

# install requirements
COPY ./Chapters/Chapter-ID/requirements.txt /work
RUN pip3 install --upgrade setuptools
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./Chapter-Name.py /work
ADD Chapters/utilities /work/base/utilities
ADD utilities /work/root/utilities

ADD ./Chapters/Chapter-ID /work

RUN find /work -name '*.py' | xargs sed -i 's/Chapters.utilities/base.utilities/g'
RUN find /work -name '*.py' | xargs sed -i 's/from utilities/from root.utilities/g'
RUN find /work -name '*.py' | xargs sed -i 's/from Chapters.Chapter-ID //g'
RUN find /work -name '*.py' | xargs sed -i 's/Chapters.Chapter-ID.//g'

ADD ./img /work/img

ENTRYPOINT ["streamlit", "run"]

CMD ["Chapter-Name.py"]
