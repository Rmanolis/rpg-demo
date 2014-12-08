//loading Lodash library in angular
var lodash = angular.module('lodash', []);
lodash.factory('_', function () {
    return window._; // assumes underscore has already been loaded on the page
});


var app = angular.module('app', ['ngRoute', 
    'ngAnimate','ngDragDrop',
    'timer',
    'ui.bootstrap',
    'facebook'
]);


app.run(function($rootScope,$location,UserSrv){
    // enumerate routes that don't need authentication
    var routesThatDontRequireAuth = ['/login', '/register'];

    // check if current location matches route
    var routeClean = function (route) {
        return _.find(routesThatDontRequireAuth,
            function (noAuthRoute) {
                return route === noAuthRoute;
            });
    };

    $rootScope.$on('$routeChangeStart', function (event, next, current) {
       /*
        *
        *
       UserSrv.getIsIn().error(function(){
            if (!routeClean($location.url())) {
                // redirect back to login
                $location.path('/login');
            } 
        }) 
         */
    });
});


app.config(function ($routeProvider, FacebookProvider) {
    FacebookProvider.init('669039869884239')
    $routeProvider
        .when('/', {
            templateUrl: 'static/app/pages/home.html',
            controller: 'HomeCtrl'
        })

        .when('/login', {
            templateUrl: 'static/app/pages/user/login.html',
            controller: 'LoginCtrl'
        })

        .when('/register', {
            templateUrl: 'static/app/pages/user/register.html',
            controller: 'RegisterCtrl'
        })

        .when('/scrolls', {
          templateUrl: 'static/app/pages/scroll/scrolls.html',
          controller: 'ScrollsCtrl'
        })

        .when('/inventories',{
          templateUrl: 'static/app/pages/inventory/inventories.html',
          controller: 'InventoriesCtrl'
         })
        
});

