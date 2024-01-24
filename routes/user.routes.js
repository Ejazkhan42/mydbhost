const express = require('express');
const router = express.Router();
const userController = require('../controllers/user.controller');

router
    .get('/', userController.get)
    .get('/:id', userController.getById)
    .post('/', userController.create)
    .put('/:id', userController.update)
    .delete('/:id', userController._delete)
    .get('/:username/:password',userController.username);

module.exports = router;
