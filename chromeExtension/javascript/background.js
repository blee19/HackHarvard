// Called when the user clicks on the browser action.
chrome.browserAction.onClicked.addListener(function(tab) {
  // Send a message to the active tab
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    var hackathonStartTime = 1477094400000; //in ms
    chrome.history.search({text:'', startTime: hackathonStartTime, maxResults:10000, }, function(history) {
      console.log(history);
    });
  });
});
