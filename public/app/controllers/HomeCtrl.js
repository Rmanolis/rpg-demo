app.controller('HomeCtrl', function($scope, Facebook){
  
          $scope.login = function () {
            Facebook.login(function(response) {
              if (response.status == 'connected') {
                $scope.status = 'yes';
              } else {
                $scope.status = 'no';
              }
            });
          };

});
