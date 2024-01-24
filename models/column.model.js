const { Model, DataTypes } = require('sequelize');

const _COLUMN_TABLE = 'columns';

class Column extends Model {
    static config(sequelize) {
        return {
            sequelize,
            tableName: _COLUMN_TABLE,
            modelName: 'Column',
            timestamps: false
        }
    }
}

const ColumnSchema = {
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
    key: {
        allowNull: false,
        type: DataTypes.STRING,
        field: 'key'
    },
    required: {
        allowNull: false,
        type: DataTypes.BOOLEAN,
        field: 'required'
    },
    suggestions: {
        type: DataTypes.JSON,
        field: 'suggestions'
    },
    description: {
        allowNull: false,
        type: DataTypes.STRING,
        field: 'description'
    },
    tableId: {
        allowNull: false,
        type: DataTypes.INTEGER,
        field: 'table_id'
    }
}

module.exports = { Column, ColumnSchema };
