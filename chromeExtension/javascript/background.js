// Called when the user clicks on the browser action.
chrome.browserAction.onClicked.addListener(function(tab) {
  // Send a message to the active tab
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    var hackathonStartTime = 1477094400000; //in ms
    chrome.history.search({text:'', startTime: hackathonStartTime, maxResults:10000, }, function(history) {
      console.log(history);

      xhr = new XMLHttpRequest();
      var url = "http://52.70.98.235:8000";
      xhr.open("POST", url, true);
      xhr.setRequestHeader("Content-type", "application/json");
      xhr.onreadystatechange = function () {
          if (xhr.readyState == 4 && xhr.status == 200) {
              console.log("message sent!");
          }
          chrome.tabs.create({"url": "http://52.70.98.235"});
      }
      var data = JSON.stringify(history);
      xhr.send(data);
    });
  });
});
