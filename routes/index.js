var express = require('express');
var router = express.Router();

/* GET home page. */
// FirebaseUI config.
var firebase = require('./firebase.js');
router.get('/', function(req, res) {
  res.render('index',{title: 'Motivator'});
});
router.get('/list', function(req,res){
	res.render('list');
})
module.exports = router;
