app.controller('NavigatorDomainCtrl', function($scope,$routeParams,$upload,
      $location, DomainSrv, UserSrv,CommunicationSrv){
  $scope.user = {};
  $scope.domain = {};
  $scope.users_joined=[];
  $scope.type_of_files = [];
  $scope.type_of_file="character";
  $scope.show_tof="character";
  var domain_id = $routeParams.domain_id;
 
  DomainSrv.getDomain(domain_id).success(function(domain){
     $scope.domain = domain;
     UserSrv.getCurrent().success(function(user){
      $scope.user = user;
      if(user.id !== domain.user.$oid){
        $location.path('/domains');
      }
     });
  });

  DomainSrv.getUsersInDomain(domain_id).success(function(users){
     $scope.users_joined = users;
  });

  DomainSrv.getTypeOfFiles().success(function(tofs){
    console.log(tofs);
    $scope.type_of_files = tofs;

  });

  $scope.show_files= function(){
    DomainSrv.getFiles(domain_id,$scope.show_tof).success(function(data){
      $scope.files_in_domain = data;
    })
  }
  $scope.show_files();  

  $scope.sendToOthers = function(file){
        CommunicationSrv.sendFile(domain_id,file._id.$oid,
        file.type_of_file);
  }

  socket.on('send-file',function(data){
    if(data.domain_id == domain_id){
      if(data.type_of_file == "character" ||
        data.type_of_file == "place"){
          $scope.choosen_image= "/domains/"+domain_id+'/files/'+data.file_id;
      }else{
          $scope.choosen_sound= "/domains/"+domain_id+'/files/'+data.file_id;
      }
    }

  });

  $scope.uploadFile = function(file){
     if (file != null) {
          $upload.upload({
            url: '/domains/'+domain_id +'/files/',
            method:'POST',
            data:{'name':$scope.name,
            'type_of_file':$scope.type_of_file},
            file: file,        
            progress: function(e){}
          }).error(function(data) {
            // file is uploaded successfully
            alert(data);
          }).success(function(){
            $scope.name = "";
            $scope.myFile = null;
            $scope.show_files();
          }); 
     }else{
        alert('Add file');
     }

  }

 



});
