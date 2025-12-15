// mathjax.js
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"], ["$", "$"]], // Enable $...$ for inline math
    displayMath: [["\\[", "\\]"], ["$$", "$$"]], // Enable $$...$$ for block math
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*",
    processHtmlClass: "arithmatex"
  }
};
document$.subscribe(() => { 
  MathJax.typesetPromise() 
})