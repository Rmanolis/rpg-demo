app.factory('InventorySrv', function($http){
  var obj = {};

  obj.getInventories = function(){
    return $http.get('https://178.62.126.138/inventories?callback=JSON_CALLBACK');
  }

  obj.postInventory = function(name){
    return $http.post('https://178.62.126.138/inventories/?callback=JSON_CALLBACK', {'name':name});
  }
  
  obj.deleteInventory = function(inventory_id){
    return $http.delete('https://178.62.126.138/inventories/'+inventory_id + '?callback=JSON_CALLBACK');
  }

  obj.getScrollsFromInventory = function(inventory_id){
    return $http.get('https://178.62.126.138/inventories/'+inventory_id +'/scrolls?callback=JSON_CALLBACK');
  }

  obj.putScrollToAnotherInventory= function(
      from_inv_id,to_inv_id, scroll_id){
    return $http.put('https://178.62.126.138/inventories/'+from_inv_id + 
        '/scrolls/'+scroll_id + '/inventories/' + to_inv_id + '?callback=JSON_CALLBACK');
  }

      

  return obj

});
