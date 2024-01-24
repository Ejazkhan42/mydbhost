const { Sequelize } = require('sequelize');

const  { config } = require('./config');
const setupModels = require('../models');
  
const sequelize = new Sequelize(
    config.dbName, // name database
    config.dbUser, // user database
    config.dbPassword, // password database
    {
      host: config.dbHost,
      dialect: 'postgresql',
      dialectOptions: {
        ssl: {
            require: true,
          }}
      
       
    }
  );

sequelize.sync();
setupModels(sequelize);

module.exports = sequelize;

