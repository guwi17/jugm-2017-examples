FROM guwi17/weblogic-base:latest 

WORKDIR /home/oracle

USER oracle

ADD wls.jar add-datasource.py create-demo-wls-domain.py ./

ENV CONFIG_JVM_ARGS=-Djava.security.egd=file:/dev/./urandom

RUN $MW_HOME/oracle_common/common/bin/wlst.sh create-demo-wls-domain.py

# ADD postgresql-42.1.4.jar 

EXPOSE 7001

CMD [ "./domains/demo-wls/startWebLogic.sh" ]

