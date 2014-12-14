app.controller('ListDomainsCtrl', function($scope,$location, DomainSrv, UserSrv){
  
  $scope.user={};

  UserSrv.getCurrent().success(function(user){
    $scope.user=user;

  });

  
  $scope.domains=[];

  function get_domains(){
    DomainSrv.getDomains().success(function(domains){
      $scope.domains = domains
    
    });
  }

  get_domains();


  $scope.navigateDomain = function(domain){
    console.log(JSON.stringify(domain));
    $location.path('/domains/'+domain._id.$oid+'/navigate');
    
  }

  $scope.joinDomain = function(domain){
    console.log(JSON.stringify(domain));
    DomainSrv.joinDomain(domain._id.$oid).success(function(){
      $location.path('/domains/'+domain._id.$oid+'/join');
    });
  }
  


});
