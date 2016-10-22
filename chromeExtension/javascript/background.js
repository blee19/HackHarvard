var hackathonEndTime = 1477227600000;
var hackathonStartTime = 1477094400000;

var totalHistoryListenerPort = 8000;
var singleItemListenerPort = 8010;

var landingURL = "http://52.70.98.235";

// Launch analytics site when the user clicks on icon
chrome.browserAction.onClicked.addListener(function(tab) {
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    chrome.tabs.create({"url": landingURL});
  });
});

// get the user's name (hopefully unique.  I'm not checking that shit)
function promptName() {
  var name = prompt("Please enter your name", "");
  if (name != null) { return name; }
  return promptName();
}

// Check whether this is the first installation
chrome.runtime.onInstalled.addListener(function(details){
  if(details.reason == "install"){
    name = promptName();
    chrome.storage.sync.set({'name': name}, function(){
      // sendHistoryToServer('',10000,8000);
      console.log("sending hackathon history");
    });
  }
});

//each time you load a page, update the server
chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    if( request.message === "page_loaded_action" ) {
      sendHistoryToServer('',1,singleItemListenerPort);
      console.log("sending single item");
    }
  }
);

//helper function to be called by virtually all history queries
function sendHistoryToServer(text, maxResults, port) {
  chrome.history.search({text:text, startTime: hackathonStartTime, endTime: hackathonEndTime, maxResults:maxResults}, function(history) {

    xhr = new XMLHttpRequest();
    var url = landingURL+ ":" + port;
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            console.log("send successful!");
        }
    }

    chrome.storage.sync.get('name', function(dict) {
      var data = JSON.stringify({'history': history, 'name': dict['name']});
      console.log(data);
      xhr.send(data);
    });
  });
}
