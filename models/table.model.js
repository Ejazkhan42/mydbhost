const { Model, DataTypes } = require('sequelize');

const TABLE_TABLE = 'tables';

class Table extends Model {
    static config(sequelize) {
        return {
            sequelize,
            tableName: TABLE_TABLE,
            modelName: 'Table',
            timestamps: false
        }
    }
}

const TableSchema = {
    id: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        type: DataTypes.INTEGER
    },
    name: {
        allowNull: false,
        type: DataTypes.STRING,
        field: 'name'
    },
    userId: {
        allowNull: false,
        type: DataTypes.INTEGER,
        field: 'user_id'
    }
}

module.exports = { Table, TableSchema };
