const { Model, DataTypes } = require('sequelize');

const USER_TABLE = 'users';

class User extends Model {
    static config(sequelize) {
        return {
            sequelize,
            tableName: USER_TABLE,
            modelName: 'User',
            timestamps: false
        }
    }
}

const UserSchema = {
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
    username: {
        allowNull: false,
        type: DataTypes.STRING,
        field: 'username'
    },
    password:{
        allowNull:false,
        type:DataTypes.STRING,
        field:'pasword'
    },
    email:{
        allowNull:false,
        type:DataTypes.STRING,
        field:'email'
    }
}

module.exports = { User, UserSchema };
