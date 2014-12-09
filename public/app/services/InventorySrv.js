app.factory('InventorySrv', function($http){
  var obj = {};

  obj.getInventories = function(){
    return $http.get('/inventories');
  }

  obj.postInventory = function(name){
    return $http.post('/inventories/', {'name':name});
  }
  
  obj.deleteInventory = function(inventory_id){
    return $http.delete('/inventories/'+inventory_id);
  }

  obj.getScrollsFromInventory = function(inventory_id){
    return $http.get('/inventories/'+inventory_id +'/scrolls');
  }

  obj.putScrollToAnotherInventory= function(
      from_inv_id,to_inv_id, scroll_id){
    return $http.put('/inventories/'+from_inv_id + 
        '/scrolls/'+scroll_id + '/inventories/' + to_inv_id);
  }

      

  return obj

});
