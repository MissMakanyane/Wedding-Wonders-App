document.getElementById("add-button").addEventListener("click", function() {
    var data = prompt("Enter data to add:");

    // Send a POST request to the server to add the data
    fetch("/add", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: "data=" + encodeURIComponent(data)
    })
    .then(function(response) {
        if (response.ok) {
            alert("Data added successfully");
        } else {
            throw new Error("Failed to add data");
        }
    })
    .catch(function(error) {
        alert(error.message);
    });
});

document.getElementById("delete-button").addEventListener("click", function() {
    var data = prompt("Enter data to delete:");

    // Send a POST request to the server to delete the data
    fetch("/delete", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: "data=" + encodeURIComponent(data)
    })
    .then(function(response) {
        if (response.ok) {
            alert("Data deleted successfully");
        } else {
            throw new Error("Failed to delete data");
        }
    })
    .catch(function(error) {
        alert(error.message);
    });
});




document.getElementById("add-button").addEventListener("click", function() {
    var data = prompt("Enter data to add:");

    if (data) {
        // Create a new table row
        var row = document.createElement("tr");

        // Create ID cell (optional)
        var idCell = document.createElement("td");
        idCell.textContent = ""; // Assign an ID if needed
        row.appendChild(idCell);

        // Create data cell
        var dataCell = document.createElement("td");
        dataCell.textContent = data;
        row.appendChild(dataCell);

        // Create action cell
        var actionCell = document.createElement("td");
        var deleteButton = document.createElement("button");
        deleteButton.textContent = "Delete";
        deleteButton.addEventListener("click", function() {
            row.parentNode.removeChild(row);
        });
        actionCell.appendChild(deleteButton);
        row.appendChild(actionCell);

        // Append the row to the table body
        document.getElementById("data-table").getElementsByTagName("tbody")[0].appendChild(row);
    }
});

document.getElementById("delete-button").addEventListener("click", function() {
    var data = prompt("Enter data to delete:");

    if (data) {
        var tableBody = document.getElementById("data-table").getElementsByTagName("tbody")[0];
        var rows = tableBody.getElementsByTagName("tr");

        for (var i = 0; i < rows.length; i++) {
            var dataCell = rows[i].getElementsByTagName("td")[1]; // Assuming second column is the data column

            if (dataCell.textContent === data) {
                tableBody.removeChild(rows[i]);
                break;
            }
        }
    }
});