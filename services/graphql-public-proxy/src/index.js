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

const link = new HttpLink({ uri: 'http://localhost:3085/graphql', fetch });

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
        graphiqlExpress({ endpointURL: '/graphql' })(req, res, next)
      }

    },
  );
  
  app.listen(3000, () => {
    console.log('Go to http://localhost:3000/graphql to run queries!');
  });
});
