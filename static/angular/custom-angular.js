
var app = angular.module('HomeApp', []);
  
 app.controller('homeController', function($scope) {
     $scope.message = 'I am the homepage';
 });




 app.controller("Coachings", function ($scope, $http) {
    $scope.init = function () {
        $scope.getCoachinglist();
    }
    $scope.filterObject = {}
    $scope.citySelected = function() {
        var selectedCity = $scope.selectedCity;
        if (selectedCity) {
            $scope.filterObject["city"] = selectedCity  
        }
    };
    $scope.courseSelected = function() {
        var selectedCourse = $scope.selectedCourse;
        if (selectedCourse) {
            $scope.filterObject["course"] = selectedCourse  
        }
    };

    $scope.feeTypeSelected = function() {
        var selectedFeeType = $scope.selectedFeeType;
        if (selectedFeeType) {
            $scope.filterObject["feetype"] = selectedFeeType  
        }
    };
    $scope.cityList = ['Noida', 'Delhi']
    $scope.courseList = ['Science', 'Comerse']
    $scope.feeTypeList = ['Full-Course', 'Month']
    $scope.fee_value = 100
    $scope.location_range = 5
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition((position) => {
            debugger;
            if("coords" in position){
                $scope.filterObject["client_location"] = position.coords
            }
            
        });
    } else {
        alert("Geolocation is not supported by this browser.");
    }
    $scope.FeeChange = function() {
        if($scope.fee_value > 100) {
            $scope.filterObject["feet"] = $scope.fee_value
        }
    }
    $scope.locationChange = function() {
        if($scope.location_range > 5) {
            $scope.filterObject["location_within"] = $scope.location_range
        }
    }
    
    $scope.filterCoaching = function() {
        debugger;
        $http({
            url:"/api/coachings/search/",
            method: "GET",
            params: $scope.filterObject
        })
        .then(function (response) {
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
        if($scope.pageUrl){
            $http.get($scope.pageUrl)
            .then(function (response) {
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
            $scope.nextPage =  response.data.next
            $scope.previousPage = response.data.previous
            $scope.getCoachinglist = response.data.results
        });
    }
});