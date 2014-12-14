app.factory('CommunicationSrv', function($http){
  var obj={};
  
  obj.sendFile = function(domain_id,file_id,type_of_file){
    return $http.post(socket_url+'send/file',{
      "domain_id":domain_id,
      "file_id":file_id,
      "type_of_file":type_of_file});
  }

  return obj;
});
