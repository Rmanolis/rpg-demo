app.factory('UserSrv', function($http){
  var obj = {};

  obj.postLogin = function(email,password){
    return $http.post('https://178.62.126.138/users/login',
       {email: email,
      'password':password});
  }

  obj.getIsIn = function(){
    return $http.get('https://178.62.126.138/users/is/in');
  }

  obj.getCurrent = function(){
    return $http.get('https://178.62.126.138/users/current');
  }

  obj.postRegister = function(user){
    return $http.post('https://178.62.126.138/users/register',user);
  }

  return obj;

});
