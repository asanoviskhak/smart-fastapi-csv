FROM postgres:16-alpine

COPY server.key /var/lib/postgresql
COPY server.crt /var/lib/postgresql

COPY root.crt /var/lib/postgresql
COPY server.crl /var/lib/postgresql

COPY ./ssl_conf.sh /usr/local/bin

RUN chown 0:70 /var/lib/postgresql/server.key && chmod 640 /var/lib/postgresql/server.key
RUN chown 0:70 /var/lib/postgresql/server.crt && chmod 640 /var/lib/postgresql/server.crt

RUN chown 0:70 /var/lib/postgresql/root.crt && chmod 640 /var/lib/postgresql/root.crt
RUN chown 0:70 /var/lib/postgresql/server.crl && chmod 640 /var/lib/postgresql/server.crl

ENTRYPOINT ["docker-entrypoint.sh"] 

CMD [ "-c", "ssl=on" , "-c", "ssl_cert_file=/var/lib/postgresql/server.crt", "-c",\
    "ssl_key_file=/var/lib/postgresql/server.key", "-c", "ssl_ca_file=/var/lib/postgresql/root.crt","-c","ssl_crl_file=/var/lib/postgresql/server.crl"]