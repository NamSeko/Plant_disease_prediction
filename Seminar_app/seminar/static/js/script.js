const dropZone = document.getElementById('drop-zone')

document.getElementById('file_input').addEventListener('change', (event) => {
    const files = event.target.files;
    hanleFile(files);
});

localStorage.setItem('selectedImage', '');

const img = document.getElementById("place_image");

function hanleFile(files) {
    for (let i = 0; i < files.length; i++) {
        const file = files[i];
        if(file.type.startsWith('image/')) {
            const reader = new FileReader();
            reader.readAsDataURL(file);
            reader.onload = () => {
                img.src = reader.result;
                localStorage.setItem('selectedImage', e.target.result);
            };
        }else{
            alert('Chỉ chấp nhận tệp hình ảnh !!!');
        }
    }
};

const selectedImage = localStorage.getItem('selectedImage');
if (selectedImage) {
    img.src = selectedImage;
};