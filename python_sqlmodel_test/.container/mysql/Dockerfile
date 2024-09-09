FROM mysql:8.0

ENV MYSQL_DATABASE=test_db \
  MYSQL_USER=developer \
  MYSQL_PASSWORD=password \
  MYSQL_ROOT_PASSWORD=password \
  TZ=Asia/Tokyo

COPY ./conf.d/my.cnf /etc/mysql/conf.d/my.cnf
RUN chmod 644 /etc/mysql/conf.d/my.cnf