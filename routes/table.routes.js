const express = require('express');
const router = express.Router();
const tableController = require('../controllers/table.controller');

router
    .get('/', tableController.get)
    .get('/:id', tableController.getById)
    .post('/', tableController.create)
    .put('/:id', tableController.update)
    .delete('/:id', tableController._delete);

module.exports = router;
