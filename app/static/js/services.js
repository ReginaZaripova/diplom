var searchServices = angular.module('searchServices', ['ngResource']);

searchServices.factory('Courses', ['$resource',
  function($resource){
    return $resource('phones/:phoneId.json', {}, {
      query: {method:'GET', params:{coursId:'courses'}, isArray:true}
    });
  }]);