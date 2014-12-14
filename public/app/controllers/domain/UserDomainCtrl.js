app.controller('UserDomainCtrl', function($scope,$routeParams,
      $location, 
      DomainSrv, 
      UserSrv){
  
  $scope.user = {};
  $scope.domain = {};
  $scope.users_joined=[];
  var domain_id = $routeParams.domain_id;
  $scope.domain = {};  
  DomainSrv.getDomain(domain_id).success(function(domain){
     $scope.domain = domain;
     UserSrv.getCurrent().success(function(user){
      $scope.user = user;
    });
  });

  DomainSrv.getUsersInDomain(domain_id).success(function(users){
        
    angular.forEach(users, function(user){
       $scope.users_joined.push(user);

    });
     
  });

  socket.on('send-file',function(data){
      if(data.domain_id == domain_id){
        if(data.type_of_file == "character" ||
          data.type_of_file == "place"){
           $scope.$apply(function()
            {
            $scope.choosen_image= "/domains/"+domain_id+'/files/'+data.file_id;
            });
            console.log(JSON.stringify(data));
             console.log($scope.choosen_image);
        }else{
            $scope.choosen_sound= "/domains/"+domain_id+'/files/'+data.file_id;
        }
      }
  })


})
