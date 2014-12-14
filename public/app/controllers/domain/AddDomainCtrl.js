app.controller('AddDomainCtrl', function($scope,$location, DomainSrv){
  
  $scope.add_domain = function(name){
    DomainSrv.postDomain(name).success(function(){
      alert('Succesfull added');
      $location.path('/domains');
    });
  }

});
