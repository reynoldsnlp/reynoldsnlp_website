// $Id: ajax.js,v 1.12 2007-11-24 06:22:28 dm Exp $
// This supports opening links in a new window without
// using the target="_blank" attribute, which is not valid strict xhtml
// If the user does not have javascript, the link simply opens in 
// the same window, so full backwards compatibility.
// Source: http://www.brucelawson.co.uk/2005/opening-links-in-new-windows-in-xhtml-strict/

function externalLinks() {
if (!document.getElementsByTagName) return;
var anchors = document.getElementsByTagName("a");
for (var i=0; i<anchors .length; i++) {
var anchor = anchors[i];
if (anchor.getAttribute("href") && anchor.getAttribute("rel") == "external") {
anchor.target = "_blank";
anchor.title = (anchor.title != "") ? anchor.title+" (opens in a new window)" : "opens in a new window";
anchor.className = (anchor.className != "") ? anchor.className+' external' : 'external';
}
}
}
window.onload = externalLinks;

