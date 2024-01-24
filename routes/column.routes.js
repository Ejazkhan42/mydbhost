const express = require('express');
const router = express.Router();
const column=require('../models/column.model')
const dynamicColumnController = require('../controllers/Column.controller');

router
    .get('/', dynamicColumnController.get)
    .get('/:id', dynamicColumnController.getById)
    .post('/', dynamicColumnController.create)
    .put('/:id', dynamicColumnController.update)
    .delete('/:id', dynamicColumnController._delete);

module.exports = router;
