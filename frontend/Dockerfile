FROM node:13.12.0-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json ./
COPY package-lock.json ./
COPY public public
COPY src src

RUN npm install

EXPOSE 3000
CMD npm run start