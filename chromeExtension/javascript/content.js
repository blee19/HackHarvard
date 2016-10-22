chrome.runtime.sendMessage({message: "page_loaded_action"}, function() {
  console.log("sent");
});
