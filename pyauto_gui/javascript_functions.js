function getElementXPath(element) {
  if (element.id !== '') {
    // If the element has an id, use it in the XPath (faster)
    return 'id("' + element.id + '")';
  }
  
  if (element === document.body) {
    return '/html/body';
  }
  //get xpath
   let xpath7 =  "/html/body/div[1]/div/div[3]/div[2]/div/main/div/div[1]/div/div/div/nav/div/span[2]/div/a/p/span" 
   
    let element7 = document.evaluate(xpath5, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; 
    
    if (element10) {
                  element10.click();
                } else {
                  console.log("Element not found!")}
///html/body/div[1]/div/div[3]/div[2]/div/main/div/div[1]/div/div/div/nav/div/span[1]/div/a/p/span

function getElementXPath(element) {
    var paths = [];
    // Loop through the element's ancestors to construct the full XPath
    while (element !== null && element.nodeType === Node.ELEMENT_NODE) {
        var path = element.nodeName.toLowerCase();  // Get the element's tag name
        var sibling = element;
        var siblingCount = 1;
        // Count how many sibling elements share the same tag name
        while (sibling.previousElementSibling) {
            sibling = sibling.previousElementSibling;
            if (sibling.nodeName.toLowerCase() === element.nodeName.toLowerCase()) {
                siblingCount++;
            }
        }      
            if (siblingCount > 1) {
                path += '[' + siblingCount + ']'; // Add position if there are other siblings with the same tag name
            }
        

        paths.unshift(path);  // Add the current path to the front of the array
        element = element.parentNode;  // Move up to the parent element
    }

    return paths.length ? '/' + paths.join('/') : null; // Join all the paths with '/'
}
/html/body/div[1]/div/div[3]/div[2]/div/main/div/div[1]/div/div/div/nav/div/span[1]/div/a/p/span



//revised for html
//output
/html/body/div[1]/div/div[3]/div[2]/div[2]/article/div/div/section/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/span/div/div/div/div/div/p/a

function getElementXPath(element) {
    var paths = [];
    // Loop through the element's ancestors to construct the full XPath
    while (element !== null && element.nodeType === Node.ELEMENT_NODE) {
        var path = element.nodeName.toLowerCase();  // Get the element's tag name
        var sibling = element;
        var siblingCount = 1;

        // Count how many sibling elements share the same tag name
        while (sibling.previousElementSibling) {
            sibling = sibling.previousElementSibling;
            if (sibling.nodeName.toLowerCase() === element.nodeName.toLowerCase()) {
                siblingCount++;
            }
        }

        if (siblingCount > 1) {
            path += '[' + siblingCount + ']'; // Add position if there are other siblings with the same tag name
        }

        paths.unshift(path);  // Add the current path to the front of the array
        element = element.parentNode;  // Move up to the parent element
    }

    // Ensure we include the <html> and <body> elements in the XPath
    if (paths.length) {
        // Add /html/body to the start of the XPath
        paths.unshift('html', 'body');
    }

    return paths.length ? '/' + paths.join('/') : null; // Join all the paths with '/'
}

correct:/html/body/div[1]/div/div[3]/div[2]/div[2]/article/div/div/section/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/span/div/div/div/div/div/p/a
not correct: /html/body/div/div[2]/div[2]/article/div/div/section/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/span/div/div/div/div/div/p/a


function getElementXPath(element) {
    var paths = [];
    while (element.nodeType === Node.ELEMENT_NODE) {
        var index = 0;
        var sibling = element.previousSibling;
        while (sibling) {
            if (sibling.nodeType === Node.DOCUMENT_NODE) break;
            if (sibling.nodeName === element.nodeName) index++;
            sibling = sibling.previousSibling;
        }
        paths.unshift(element.nodeName.toLowerCase() + (index ? ":nth-of-type(" + (index + 1) + ")" : ""));
        element = element.parentNode;
    }
    return paths.length ? "/" + paths.join("/") : null;
}


// Attach an event listener to document to capture click events
document.addEventListener("click", function(event) {
    var xpath = getElementXPath(event.target);  // Get the XPath of the clicked element
    console.log("XPath of the clicked element:", xpath);
    alert("XPath: " + xpath);  // Optional: Show an alert with the XPath
});



