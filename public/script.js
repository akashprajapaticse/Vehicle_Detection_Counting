// Upload a video file to Flask
document.getElementById('uploadBtn').addEventListener('click', () => {
    const input = document.createElement('input');
    input.type = 'file';
    input.accept = 'video/*';

    input.onchange = async (event) => {
        const file = event.target.files[0];
        if (!file) return;

        const formData = new FormData();
        formData.append('videoFile', file);

        try {
            const response = await fetch('http://127.0.0.1:5000/upload', {
                method: 'POST',
                body: formData
            });
            const text = await response.text();
            console.log(text);
        } catch (error) {
            console.error('Error uploading file:', error);
        }
    };

    input.click();
});

// Stop detection
document.getElementById('stopBtn').addEventListener('click', async () => {
    try {
        const response = await fetch('http://127.0.0.1:5000/stop', {
            method: 'POST'
        });
        const text = await response.text();
        console.log(text);
    } catch (error) {
        console.error('Error stopping detection:', error);
    }
});

// Test route
document.getElementById('testBtn').addEventListener('click', async () => {
    try {
        const response = await fetch('http://127.0.0.1:5000/test');
        const text = await response.text();
        alert(`Response from /test: ${text}`);
    } catch (error) {
        console.error('Error calling /test:', error);
    }
});
