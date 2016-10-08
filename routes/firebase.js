
var firebase = require('firebase');
/* GET users listing. */
var config = {
    apiKey: "AIzaSyDk1aO_yaVKgTi9dGwY6-rkLVX2nka-QdU",
    authDomain: "motivator-a8e20.firebaseapp.com",
    databaseURL: "https://motivator-a8e20.firebaseio.com",
    storageBucket: "",
    messagingSenderId: "24548565731"
  };
firebase.initializeApp(config);
/*firebase auth*/


module.exports = firebase;