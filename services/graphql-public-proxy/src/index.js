const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const { graphqlExpress, graphiqlExpress } = require('apollo-server-express');
const {
  makeRemoteExecutableSchema,
  introspectSchema,
  transformSchema,
  FilterRootFields } = require('graphql-tools');
const {HttpLink} = require('apollo-link-http');
const fetch = require('node-fetch');
const fs = require('fs');

const CODA_GRAPHQL_HOST = process.env["CODA_GRAPHQL_HOST"] || "localhost";
const CODA_GRAPHQL_PORT = process.env["CODA_GRAPHQL_PORT"] || 3085;
const CODA_GRAPHQL_PATH = process.env["CODA_GRAPHQL_PATH"] || "/graphql";
const EXTERNAL_PORT = process.env["EXTERNAL_PORT"] || 3000;

let graphqlUri = "http://" + CODA_GRAPHQL_HOST + ":" + CODA_GRAPHQL_PORT + CODA_GRAPHQL_PATH;

const link = new HttpLink({ uri: graphqlUri, fetch });

const hiddenFields = [
  "trackedWallets",
  "currentSnarkWorker",
  "initialPeers",
  "wallet",
];

const transformers = [
  new FilterRootFields((operation, fieldName, field) => !field.isDeprecated),
  new FilterRootFields((operation, fieldName, field) => operation != 'Mutation'),
  new FilterRootFields((operation, fieldName, field) => hiddenFields.indexOf(fieldName) < 0),
];

const graphiqlString = fs.readFileSync("./index.html");

introspectSchema(link)
.then(remoteSchema => {
  return makeRemoteExecutableSchema({
    schema: remoteSchema,
    link,
  });
}).then(schema => {
  const app = express();

  app.use(cors());

  // The GraphQL endpoint
  app.use('/graphql',
    bodyParser.json(), 
    (req, res, next) => {
      if (req.headers["accept"] == "application/json") {
        graphqlExpress({ schema: transformSchema(schema, transformers) })(req, res, next)
      } else {
        res.setHeader('Content-Type', 'text/html');
        res.write(graphiqlString);
        res.end();
      }

    },
  );
  
  app.listen(EXTERNAL_PORT, () => {
    console.log('Go to http://localhost:' + EXTERNAL_PORT + '/graphql to run queries!');
  });
});
