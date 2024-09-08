document.getElementById('uploadForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const formData = new FormData(this);

    // Send the file to the backend via AJAX
    fetch('', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': '{{ csrf_token }}'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Update the uploaded files list
            updateUploadedFiles(data.files);
        }
    });
});

// Function to update the list of uploaded files dynamically
function updateUploadedFiles(files) {
    const uploadedFilesBox = document.getElementById('uploadedFilesBox');
    uploadedFilesBox.innerHTML = ''; // Clear the current list

    files.forEach(file => {
        const fileItem = document.createElement('div');
        fileItem.classList.add('file-list-item');
        fileItem.textContent = file.name;
        fileItem.addEventListener('click', function() {
            selectFileForDownload(file);
        });
        uploadedFilesBox.appendChild(fileItem);
    });
}

// Function to select a file for download
function selectFileForDownload(file) {
    const selectedFilesBox = document.getElementById('selectedFilesBox');
    const fileItem = document.createElement('div');
    fileItem.classList.add('file-list-item');
    fileItem.textContent = file.name;
    selectedFilesBox.appendChild(fileItem);
}

// Filters for file types (AVI/MP4)
document.getElementById('AVI').addEventListener('click', function() {

});
document.getElementById('MP4').addEventListener('click', function() {

});
