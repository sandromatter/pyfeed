var feedTitleCounter = document.getElementById("feedTitleCounter");
var wordCountTitle = document.getElementById("wordCountTitle");

feedTitleCounter.addEventListener("keyup",function(){
  var characters = feedTitleCounter.value.split('');
  wordCountTitle.innerText = characters.length;
  if(characters.length > 40){
    feedTitleCounter.value = feedTitleCounter.value.substring(0,40);
    wordCountTitle.innerText = 40;
  }
});


var feedDescriptionCounter = document.getElementById("feedDescriptionCounter");
var wordCountDescription = document.getElementById("wordCountDescription");

feedDescriptionCounter.addEventListener("keyup",function(){
  var characters = feedDescriptionCounter.value.split('');
  wordCountDescription.innerText = characters.length;
  if(characters.length > 140){
  	feedDescriptionCounter.value = feedDescriptionCounter.value.substring(0,140);
    wordCountDescription.innerText = 140;
  }
});