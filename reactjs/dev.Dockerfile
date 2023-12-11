FROM node:20

COPY package*.json ./

RUN npm install

WORKDIR /workspace/reactjs

COPY . .

# Command to run the app
CMD ["npm", "run", "dev","--","--host"]