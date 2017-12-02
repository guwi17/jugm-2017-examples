FROM guwi17/java-base:latest 


RUN useradd --create-home oracle && \
    chown -R oracle:oracle /home/oracle

WORKDIR /home/oracle

RUN  mkdir -p oraInventory && \
     chown oracle:oracle oraInventory && \
     chmod 770 oraInventory && \
     echo 'inventory_loc=/home/oracle/oraInventory' > /etc/oraInst.loc && \
     echo 'inst_group=oracle' >> /etc/oraInst.loc

USER oracle

ENV MW_HOME=/home/oracle/wls 

ADD tmp/fmw_12.2.1.3.0_wls.jar .

RUN java -jar fmw_12.2.1.3.0_wls.jar -ignoreSysPrereqs -silent ORACLE_HOME=$MW_HOME DECLINE_AUTO_UPDATES=true "INSTALL_TYPE=WebLogic Server" \
    && rm fmw_12.2.1.3.0_wls.jar

# verify that installation was successful
RUN [ "/bin/bash", "-c", ". $MW_HOME/wlserver/server/bin/setWLSEnv.sh && \
    java weblogic.version -verbose" ]

CMD [ "bash" ]

