var array1 = ["media/coringa-gym.jpg", "media/maumau.jpg", "media/mansao-do-coringa-25-1300x752.webp"];

function updateSlider() {
    const slides = document.querySelector('.slides');
    const totalSlides = document.querySelectorAll('.slide').length;
    slides.style.transform = 'translateX(' + (-currentIndex * 100) + '%)';
}

function comeco() {
    document.getElementById('imgId').src = array1[0];
    document.form.texto.value = "0"; 
}

function mais() {
    var currentIndex = parseInt(document.form.texto.value); 
    currentIndex = (currentIndex + 1) % array1.length; 
    document.form.texto.value = currentIndex; 
    document.getElementById('imgId').src = array1[currentIndex]; 
}


function menos() {
    var currentIndex = parseInt(document.form.texto.value); 
    currentIndex = (currentIndex - 1 + array1.length) % array1.length; 
    document.form.texto.value = currentIndex; 
    document.getElementById('imgId').src = array1[currentIndex]; 
}

function regular() {
    sliderInterval = setInterval(function() {
        var currentIndex = parseInt(document.form.texto.value);
        currentIndex = (currentIndex + 1) % array1.length; 
        document.form.texto.value = currentIndex;
        document.getElementById('imgId').src = array1[currentIndex];
    }, 5000); 

}

