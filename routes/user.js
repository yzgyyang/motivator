var express = require('express');
var router = express.Router();
var firebase = require('./firebase.js');
function writeUserData(userId, name, email, imageUrl) {
  firebase.database().ref('users/' + userId).set({
    username: name,
    email: email,
    profile_picture : imageUrl
  });
}

router.get('/', function(req, res) {

// Create a storage reference from our storage service
  //var storageRef = storage.ref();
  writeUserData("test4", "dan","yy@gamil.com",null);
  res.send('respond with a resource');
});

module.exports = router;
