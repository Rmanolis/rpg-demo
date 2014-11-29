app.controller('RegisterCtrl', function($scope, $location, UserSrv){
  $scope.errors = []
  $scope.user = {
    email:'',
    username:'',
    password:''
  }
  $scope.save = function(user){
    UserSrv.postRegister(user)
      .success(function(data){
  
        if(data.errors){
          $scope.errors = data.errors;
        }else{
          $location.path('/')
        }
      });

  };

  $scope.cancel = function(){
    $location.path('/')
  };

});
