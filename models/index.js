const { Column, ColumnSchema } = require('./column.model');
const { Table, TableSchema } = require('./table.model');
const { User, UserSchema } = require('./user.model');

function setupModels(sequelize) {
   
    
    User.init(UserSchema,User.config(sequelize));
    Table.init(TableSchema,Table.config(sequelize));
     Column.init(ColumnSchema, Column.config(sequelize));
}

module.exports = setupModels;

