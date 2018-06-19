// Initialize Firebase
var config = {
apiKey: "AIzaSyCMLWzRotGDVmufsunvBuYmIlLrHi2Ezds",
authDomain: "aixai-db.firebaseapp.com",
databaseURL: "https://aixai-db.firebaseio.com",
projectId: "aixai-db",
storageBucket: "gs://aixai-db.appspot.com",
messagingSenderId: "235347485754"
};
firebase.initializeApp(config);

// Get a reference to the storage service, which is used to create references in your storage bucket
var storage = firebase.storage();