const { models } = require('../config/db');

class UserService {
    constructor() {}

    async username(username,password){
        const res = await models.User.findOne({
            where: {
              username: username,
              password: password,
            },
          });
          return res;

    }
    async find() {
        const res = await models.User.findAll();
        return res;
    }

    async findOne(id) {
        const res = await models.User.findByPk(id);
        return res;
    }

    async create(data) {
        const res = await models.User.create(data);
        return res;
    }

    async update(id, data) {
        const model = await this.findOne(id);
        const res = await model.update(data);
        return res;
    }

    async delete(id) {
        const model = await this.findOne(id);
        await model.destroy();
        return { deleted: true };
    }
}

module.exports = UserService;
