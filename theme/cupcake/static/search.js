(function () {
  var input = document.getElementById('manual-search');
  var results = document.getElementById('manual-results');
  var content = document.getElementById('manual-content');
  var index = window.MANUAL_INDEX || [];
  var base = document.querySelector('.brand').getAttribute('href').replace(/index\.html$/, '');

  function excerpt(text, terms) {
    var lower = text.toLowerCase();
    var at = Math.min.apply(null, terms.map(function (t) { var i = lower.indexOf(t); return i < 0 ? 0 : i; }));
    var start = Math.max(at - 80, 0);
    return (start ? '…' : '') + text.slice(start, start + 220) + '…';
  }

  function show(query) {
    var terms = query.toLowerCase().split(/\W+/).filter(Boolean);
    if (!terms.length) { results.hidden = true; content.hidden = false; return; }
    var found = index.filter(function (page) {
      var hay = (page.title + ' ' + page.text).toLowerCase();
      return terms.every(function (t) { return hay.indexOf(t) >= 0; });
    }).sort(function (a, b) {
      var score = function (p) { return terms.filter(function (t) { return p.title.toLowerCase().indexOf(t) >= 0; }).length; };
      return score(b) - score(a);
    });
    results.replaceChildren();
    var heading = document.createElement('h1');
    heading.textContent = found.length ? 'Results for “' + query + '”' : 'Nothing in the manual matches every word.';
    results.appendChild(heading);
    found.forEach(function (page) {
      var item = document.createElement('div');
      item.className = 'result';
      var link = document.createElement('a');
      link.href = base + page.url;
      link.textContent = page.title;
      var text = document.createElement('p');
      text.textContent = excerpt(page.text, terms);
      item.appendChild(link);
      item.appendChild(text);
      results.appendChild(item);
    });
    results.hidden = false;
    content.hidden = true;
  }

  input.addEventListener('input', function () { show(input.value.trim()); });
  var initial = new URLSearchParams(window.location.search).get('q');
  if (initial) { input.value = initial; show(initial); }
})();
