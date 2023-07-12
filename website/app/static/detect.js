const show_img = document.getElementById('show-img');
const predict_btn = document.getElementById('detect');

async function showImage() {
    fetch('/predict/images')
    .then(response => response.json())
    .then(data => {
        // Xử lý chuỗi đường dẫn ảnh nhận được ở đây
        // Ví dụ: hiển thị các ảnh trong một div
        show_img.innerHTML = '';
        data.forEach(url => {
        const img = document.createElement('img');
        img.src = url;
        show_img.appendChild(img);
        });
    })
    .catch(error => {
        console.error('Lỗi khi nhận chuỗi đường dẫn ảnh:', error);
    });
}

showImage()

// Thêm event cho predict button
predict_btn.addEventListener('click',() => {
    // Gửi yêu cầu GET đến server
    fetch('/predict/detect')
    .then(response => response.json())
    .then(data => {
        // Xử lý dữ liệu nhận được ở đây
        // Ví dụ: hiển thị kết quả dự đoán
        console.log(data);
    }
    )
    .catch(error => {
        console.error('Lỗi khi nhận kết quả dự đoán:', error);
    }
    );
});

setInterval(() => {
    showImage();
}, 10000);