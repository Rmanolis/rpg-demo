app.factory('DomainSrv', function($http ){
  var obj = {}
  
  obj.getDomains = function(){
    return $http.get('/domains/');
  }

  obj.getDomain = function(domain_id){
    return $http.get('/domains/'+domain_id);
  }

  obj.postDomain = function(name){
    return $http.post('/domains/',{'name':name});
  }

  obj.getFiles = function(domain_id,file_type){
    return $http.get('/domains/'+domain_id+'/type_of_files/'+file_type+'/files');
  }


  obj.changeFileName = function(domain_id,file_id, name){
    return $http.put('/domains/' + domain_id +
        '/files/'+ file_id,{'name':name});
  }

  obj.changeDomainName = function(domain_id,name){
    return $http.put('/domains/' + domain_id,{'name':name});
  } 

  obj.joinDomain = function(domain_id){
    return $http.get('/domains/'+domain_id+'/connect');
  }

  obj.quitDomain = function(domain_id){
    return $http.get('/domains/'+domain_id+'/quit');
  }
  obj.getUsersInDomain = function(domain_id){
    return $http.get('/domains/'+domain_id+'/users');
  }

  obj.getTypeOfFiles = function(){
    return $http.get('/type_of_files');
  }
  /*
  obj.uploadFile = function(domain_id,file,name,type_of_file){
    $upload.upload({
        url: '/domains/'+domain_id+'/files',
        method: 'POST' ,
        data: {'name':name,
        'type_of_file':type_of_file},
        file: file
      }).progress(function(evt) {
        console.log('progress: ' + parseInt(100.0 * evt.loaded / evt.total) + '% file :'+ evt.config.file.name);
      }).success(function(data, status, headers, config) {
        console.log('file ' + config.file.name + 'is uploaded successfully. Response: ' + data);
      });
  }*/


  return obj;
});

