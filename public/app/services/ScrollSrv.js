app.factory('ScrollSrv', function($http){
  var obj={};
 
  obj.postScroll = function(scroll){
    return $http.post('/scrolls/',scroll);
  }

  obj.getScroll = function(scroll_id){
    return $http.get('/scrolls/'+scroll_id);
  }

  obj.getUnfinishedScrolls = function(){
    return $http.get('/scrolls/unfinished');
  }

  return obj;
});
