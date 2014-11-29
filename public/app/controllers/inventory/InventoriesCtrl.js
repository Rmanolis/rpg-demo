app.controller('InventoriesCtrl', function($scope, InventorySrv){
  $scope.inventories = [];
  $scope.inventory_name = "";
  $scope.draggedScroll={};
  $scope.draggedFromInventoryId = "";
  function get_inventories(){
    $scope.inventories = [];
    InventorySrv.getInventories()
      .success(function(inventories){
        angular.forEach(inventories, 
            function(inventory){
            InventorySrv.getScrollsFromInventory(inventory['_id']['$oid']).
              success(function(scrolls){
                for(i=0; i< scrolls.length; i++){
                  scrolls[i].drag = true;
                }
                inventory.list = scrolls;
                $scope.inventories.push(inventory);  
              });
        });
    });
  }

  get_inventories()

  $scope.$on('reload:scrolls', function(){
   get_inventories();
 })

  $scope.onDrop = function(event,ui,to_id){
      console.log('Drop ' + $scope.draggedScroll.name);
      InventorySrv
        .putScrollToAnotherInventory(
            $scope.draggedFromInventoryId,
            to_id,
            $scope.draggedScroll.id)
  }

  $scope.onDrag = function(event,ui,item,from_id){
        $scope.draggedScroll = item;
        $scope.draggedFromInventoryId = from_id;
  }

  $scope.add_inventory = function(name){
    InventorySrv.postInventory(name).success(function(data){
      if(data.errors){
        alert(data.errors[0]);
      }else{
        $scope.inventory_name ="";
      }
    });
    get_inventories();
  }
});
