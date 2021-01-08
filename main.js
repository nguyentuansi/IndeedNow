function getJSON(url, callbackFunction) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            try {
                var responseData = JSON.parse(xmlhttp.responseText);
            } catch(error) {
                return;
            }
            callbackFunction(responseData);
        }
    };

    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}


document.addEventListener('DOMContentLoaded', (event) => {
    var container = document.getElementById("openSourceRepos");

    getJSON('repo_data.json', function(data) {
        data.forEach(function (repo) {
            var child = `
                <div>
                  <h2>
                      <a href='${repo.url}'>${repo.full_name}</a>
                  </h2>
                   <p>${repo.short_description}</p>
                   <ul>
                       <li>${repo.stars}</li>
                       <li>${repo.forks}</li>
                       <li>${repo.watchers}</li>
                   </ul>
                </div>
            `;
            container.insertAdjacentHTML('beforeend', child);
        });
    });
});