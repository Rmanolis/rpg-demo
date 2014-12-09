app.controller('LoginCtrl', function($scope,$window, $http, $location, $rootScope, UserSrv){
  
  
   $scope.login = function (email,password) {
       UserSrv.postLogin(email,password).
            success(function (data) {
              if(data.is_accepted){
                $rootScope.$broadcast("successful:login");
                $location.path('/');
              }else{
                alert('Wrong email and password');                
              }
            })
            .error(function(){
                alert('Wrong email and password');
            });
    };

   $scope.loginFromFacebook = function(){
        $window.location.href = 'http://178.62.126.138/login';
     
     
   }

});
