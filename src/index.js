const express = require('express'); 

const userRouter = require('../routes/user.routes');
const columnRouter =require('../routes/column.routes');
const tableRouter=require('../routes/table.routes')
function routerApi(app) {
  const router = express.Router();
  app.use('/api/v1', router); 
  router.use('/user', userRouter);
  router.use('/column',columnRouter);
  router.use('/table',tableRouter);
}

module.exports = routerApi;
