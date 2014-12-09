app.factory('UserSrv', function($http){
  var obj = {};

  obj.postLogin = function(email,password){
    return $http.post('https://178.62.126.138/users/login?callback=JSON_CALLBACK',
       {email: email,
      'password':password});
  }

  obj.getIsIn = function(){
    return $http.get('https://178.62.126.138/users/is/in?callback=JSON_CALLBACK');
  }

  obj.getCurrent = function(){
    return $http.get('https://178.62.126.138/users/current?callback=JSON_CALLBACK');
  }

  obj.postRegister = function(user){
    return $http.post('https://178.62.126.138/users/register?callback=JSON_CALLBACK',user);
  }

  return obj;

});
