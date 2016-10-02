(function(){

  var searchBar = document.getElementById("search");
  var results = document.getElementById("results");

  function getSearchResults(query){
    return fetch("/autocorrect?string="+query)
           .then(function(txt){
             return txt.text();
           })
           .then(function(body){
             return new Promise(function(res, rej){
                 var bdy = JSON.parse(body);
                 if(!bdy.none)
                    res(bdy.results)
                 else
                    rej(bdy.results)
             });
           });
  }

  function showResults(results){
    var resultsField = document.getElementById("results");
    resultsField.innerHTML = "";
     if(!results)
        resultsField.innerHTML = "<li><b> No Results Found! </b></li>";
     else{
        resultsField.innerHTML ="<li>"+ results+"</li>";
     }
  }

  function init(){
     var search = document.getElementById("search");
     search.addEventListener('change', function(){
        var string = search.value.toLowerCase();
        console.log(string);
        getSearchResults(string).then(function(value){
          showResults(value.toUpperCase());
        });
     }, false);
  }

  init();


})();
