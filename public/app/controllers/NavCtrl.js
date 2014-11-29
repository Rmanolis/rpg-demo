app.controller('NavCtrl', function($scope, $http, UserSrv){
  
  $scope.sitemap = [];
  $scope.username = '';
  $scope.id = '';

  var getNavigation = function() {
   
    $http.get('/sitemap').success(function(data) {
      return $scope.sitemap = data;
    });
    UserSrv.getCurrent().success(function(user){
      $scope.username = user.username;
      $scope.id = user.id;
    })

  };

  getNavigation();
  $scope.$on("successful:login", getNavigation);
  $scope.$on("successful:logout", getNavigation);

  socket.on('new-scroll', function(data){
    if($scope.id == data.user_id){
      alert("The scroll " + data.scroll_name + " is ready ");
      $scope.$broadcast("reload:scrolls");
    }
  });

});
