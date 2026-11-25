(function () {
  var badge = document.getElementById('manual-version');
  var picker = document.getElementById('manual-versions');
  var older = document.getElementById('manual-older');
  var current = badge.dataset.version;
  var page = window.location.pathname.split('/').pop() || 'index.html';
  if (window.location.protocol === 'file:') { return; }
  fetch('../versions.json', { cache: 'no-store' })
    .then(function (response) { if (!response.ok) { throw new Error(); } return response.json(); })
    .then(function (data) {
      var versions = data.versions || [];
      if (versions.indexOf(current) < 0) { return; }
      versions.forEach(function (version) {
        var option = document.createElement('option');
        option.value = version;
        option.textContent = version === 'latest' ? 'latest (in development)' : version;
        option.selected = version === current;
        picker.appendChild(option);
      });
      picker.hidden = false;
      badge.hidden = true;
      picker.addEventListener('change', function () { window.location.href = '../' + picker.value + '/' + page; });
      if (data.newest && current !== 'latest' && current !== data.newest) {
        older.textContent = 'This is the manual of ' + current + '. The newest release is ' + data.newest + '.';
        older.hidden = false;
      }
    })
    .catch(function () {});
})();
