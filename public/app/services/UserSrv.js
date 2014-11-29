app.factory('UserSrv', function($http){
  var obj = {};

  obj.postLogin = function(email,password){
    return $http.post('/users/login',
       {email: email,
      'password':password});
  }

  obj.getIsIn = function(){
    return $http.get('/users/is/in');
  }

  obj.getCurrent = function(){
    return $http.get('/users/current');
  }

  obj.postRegister = function(user){
    return $http.post('/users/register',user);
  }

  return obj;

});
