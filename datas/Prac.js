var languageForm = document.getElementById("language-form");
var languageInput = document.getElementById("language-input");
var languageList = document.getElementById("language-list");

languageForm.addEventListener("submit", function(event) {
    event.preventDefault();

    var languageName = languageInput.value.trim();

    if (languageName) {
        var listItem = document.createElement("li");
        var languageSpan = document.createElement("span");
        languageSpan.textContent = languageName;
        listItem.appendChild(languageSpan);

        var updateButton = document.createElement("button");
        updateButton.textContent = "Update";
        updateButton.addEventListener("click", function() {
            var newLanguageName = prompt("Enter new language name:", languageName);

            if (newLanguageName) {
                languageSpan.textContent = newLanguageName;
            }
        });
        listItem.appendChild(updateButton);

        var deleteButton = document.createElement("button");
        deleteButton.textContent = "Delete";
        deleteButton.addEventListener("click", function() {
            listItem.parentNode.removeChild(listItem);
        });
        listItem.appendChild(deleteButton);

        languageList.appendChild(listItem);

        languageInput.value = "";
    }
});