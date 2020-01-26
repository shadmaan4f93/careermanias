
var app = angular.module('HomeApp', []);
  
 app.controller('homeController', function($scope) {
     $scope.message = 'I am the homepage';
 });


 app.controller("Coachings", function ($scope, $http) {
    $scope.init = function () {
        $scope.getCoachinglist();
    }
    $scope.filterObject = {
        name:'Careermania'
    }
    $scope.filterCoaching = function(key, value) {
        $http({
            url:"/api/coachings/search/",
            method: "GET",
            params: $scope.filterObject
        })
        .then(function (response) {
            debugger;
            $scope.nextPage =  response.data.next
            $scope.previousPage = response.data.previous
            $scope.getCoachinglist = response.data.results
        });
    };

    $scope.CoachingNext = function() {
        if($scope.nextPage) {
            $http.get($scope.nextPage)
            .then(function (response) {
                $scope.nextPage =  response.data.next
                $scope.previousPage = response.data.previous
                $scope.getCoachinglist = response.data.results
            });
        }
        
    };

    $scope.CoachingPrevious = function() {
        if($scope.previousPage){
            $http.get($scope.previousPage)
            .then(function (response) {
                $scope.nextPage =  response.data.next
                $scope.previousPage = response.data.previous
                $scope.getCoachinglist = response.data.results
            });
        }
        
    };

    $scope.CoachingByPageNumber = function(pageNumber) {
        $scope.pageUrl = "http://127.0.0.1:8000/api/coachings/all/?page=" + pageNumber
        debugger
        if($scope.pageUrl){
            $http.get($scope.pageUrl)
            .then(function (response) {
                debugger;
                $scope.nextPage =  response.data.next
                $scope.previousPage = response.data.previous
                $scope.getCoachinglist = response.data.results
            });
        }
        
    };

    $scope.getCoachinglist = function () {
        $scope.pagination = []
        $http.get("/api/coachings/all/")
        .then(function (response) {
            $scope.pagenumber = Math.ceil(response.data.count/4)
            for (i=1; i<=$scope.pagenumber;i++){
                $scope.pagination.push(i)   
            }
            debugger;
            $scope.nextPage =  response.data.next
            $scope.previousPage = response.data.previous
            $scope.getCoachinglist = response.data.results
        });
    }
});