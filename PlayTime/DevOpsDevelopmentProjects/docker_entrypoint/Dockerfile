FROM node:alpine
COPY . /app
WORKDIR /app

COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"]

# CMD node app.js
CMD ["node", "app.js"]
