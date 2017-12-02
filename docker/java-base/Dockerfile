FROM debian:latest 

ADD jdk-8u152-linux-x64.tar.gz /usr/local

RUN rm /usr/local/jdk*/*src.zip

RUN ln -s /usr/local/jdk* /usr/local/jdk

RUN [ "/bin/bash", "-c", "for N in /usr/local/jdk/bin/* ; do ln -s $N /usr/local/bin/ ; done " ]

ENV JAVA_HOME=/usr/local/jdk

CMD [ "bash" ]

