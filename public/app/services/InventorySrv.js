app.factory('InventorySrv', function($http){
  var obj = {};

  obj.getInventories = function(){
    return $http.jsonp('https://178.62.126.138/inventories');
  }

  obj.postInventory = function(name){
    return $http.post('https://178.62.126.138/inventories/', {'name':name});
  }
  
  obj.deleteInventory = function(inventory_id){
    return $http.delete('https://178.62.126.138/inventories/'+inventory_id);
  }

  obj.getScrollsFromInventory = function(inventory_id){
    return $http.jsonp('https://178.62.126.138/inventories/'+inventory_id +'/scrolls');
  }

  obj.putScrollToAnotherInventory= function(
      from_inv_id,to_inv_id, scroll_id){
    return $http.put('https://178.62.126.138/inventories/'+from_inv_id + 
        '/scrolls/'+scroll_id + '/inventories/' + to_inv_id);
  }

      

  return obj

});
