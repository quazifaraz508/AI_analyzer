document.addEventListener("DOMContentLoaded", function () {
    const fileInput = document.getElementById("resume");
    const uploadBtn = document.getElementById("uploadBtn");
    const dropArea = document.getElementById("dropArea");
    const darkModeToggle = document.getElementById("darkModeToggle");
    const htmlElement = document.documentElement;

    // 1️⃣ Custom File Upload Button Behavior
    uploadBtn.addEventListener("click", function () {
        fileInput.click();
    });

    fileInput.addEventListener("change", function () {
        if (fileInput.files.length > 0) {
            uploadBtn.innerText = `Selected: ${fileInput.files[0].name}`;
        }
    });

    // 2️⃣ Drag & Drop File Upload
    if (dropArea) {
        dropArea.addEventListener("dragover", (event) => {
            event.preventDefault();
            dropArea.classList.add("border-purple-500");
        });

        dropArea.addEventListener("dragleave", () => {
            dropArea.classList.remove("border-purple-500");
        });

        dropArea.addEventListener("drop", (event) => {
            event.preventDefault();
            dropArea.classList.remove("border-purple-500");

            const files = event.dataTransfer.files;
            if (files.length > 0) {
                fileInput.files = files;
                uploadBtn.innerText = `Selected: ${files[0].name}`;
            }
        });
    }

    // 3️⃣ Dark Mode Toggle
    darkModeToggle.addEventListener("click", function () {
        if (htmlElement.getAttribute("data-theme") === "light") {
            htmlElement.setAttribute("data-theme", "dark");
            darkModeToggle.innerText = "☀️ Light Mode";
        } else {
            htmlElement.setAttribute("data-theme", "light");
            darkModeToggle.innerText = "🌙 Dark Mode";
        }
    });
});

// // job_description and intership detail
// document.addEventListener("DOMContentLoaded", function () {
//     const toggleJobInternship = document.getElementById('toggleJobInternship');
//     const jobInternshipSection = document.getElementById('jobInternshipSection');
    
//     // Event listener to toggle the visibility of Job Description and Internship Details
//     toggleJobInternship.addEventListener('change', function () {
//         if (this.checked) {
//             jobInternshipSection.classList.remove('hidden');  // Show the section
//         } else {
//             jobInternshipSection.classList.add('hidden');  // Hide the section
//         }
//     });  
// });

document.getElementById('showTextCheckbox').addEventListener('change', function() {
    var textContainer = document.getElementById('extractedTextContainer');

    // Show or hide the extracted text based on checkbox status
    if (this.checked) {
        textContainer.classList.remove('hidden');  // Show the text
    } else {
        textContainer.classList.add('hidden');  // Hide the text
    }
});


