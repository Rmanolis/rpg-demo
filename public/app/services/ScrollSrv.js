app.factory('ScrollSrv', function($http){
  var obj={};
 
  obj.postScroll = function(scroll){
    return $http.post('https://178.62.126.138/scrolls/?callback=JSON_CALLBACK',scroll);
  }

  obj.getScroll = function(scroll_id){
    return $http.get('https://178.62.126.138/scrolls/'+scroll_id + '?callback=JSON_CALLBACK');
  }

  obj.getUnfinishedScrolls = function(){
    return $http.get('https://178.62.126.138/scrolls/unfinished?callback=JSON_CALLBACK');
  }

  return obj;
});
