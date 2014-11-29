app.controller('ScrollsCtrl', function($scope, ScrollSrv){
 $scope.scrolls = [];
 $scope.new_scroll = {
  name:'',
  description:''
 }
 function get_scrolls(){
  ScrollSrv.getUnfinishedScrolls().success(function(scrolls){
    $scope.scrolls = scrolls;
  });
 }
 get_scrolls();

 $scope.$on('reload:scrolls', function(){
   get_scrolls();
 })



 $scope.add_scroll = function(scroll){
    ScrollSrv.postScroll(scroll).success(function(data){
      if(data.errors){
        alert(data.errors[0]);
      }else{
         $scope.new_scroll = {
            name:'',
            description:''
          }
        get_scrolls();
      }
    });
 }

});
