
var app = angular.module('myApp', []);
  
 app.controller('homeController', function($scope) {
     $scope.message = 'I am the homepage';
 });


 app.controller("ProjectList", function ($scope, $http) {
    $scope.message= "Project List"
    $scope.init = function () {
        $scope.getProjectlist();
    }
    $scope.getProjectlist = function () {
        $http.get("/api/projects/")
        .then(function (response) {
            $scope.getProjectlist = response.data
        });
    }
});