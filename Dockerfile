FROM tomcat:9
LABEL app=back
COPY /target/*.war /usr/local/tomcat/webapps/dev.war