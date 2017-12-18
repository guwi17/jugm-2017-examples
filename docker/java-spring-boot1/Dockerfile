FROM guwi17/java-base 

RUN mkdir /home/app

WORKDIR /home/app

ADD SpringBootEx1-1.0-SNAPSHOT.jar .

EXPOSE 8080

CMD [ "java", "-Xmx1024m", "-jar", "SpringBootEx1-1.0-SNAPSHOT.jar" ]

