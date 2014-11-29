app.controller('LoginCtrl', function($scope, $location, $rootScope, UserSrv){
  
  
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

});
