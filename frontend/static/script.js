var myText = document.getElementById("myText");
var wordCount = document.getElementById("wordCount");

myText.addEventListener("keyup",function(){
	var characters = myText.value.split('');
  wordCount.innerText = characters.length;
  if(characters.length > 140){
  	myText.value = myText.value.substring(0,140);
    wordCount.innerText = 140;
  }
});

$(function() {
  $('#feedColorPickerInput').colorpicker({
  });
});