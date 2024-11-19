const slides = document.querySelector('.slides');
        const slideElements = document.querySelectorAll('.slide');
        const dotContainer = document.querySelector('.dot-container');
        let currentIndex = 0;
        let slideInterval;


        slideElements.forEach((_, index) => {
            const dot = document.createElement('div');
            dot.classList.add('dot');
            if (index === 0) dot.classList.add('active');
            dot.addEventListener('click', () => goToSlide(index));
            dotContainer.appendChild(dot);
        });

        const dots = document.querySelectorAll('.dot');

        function updateSlider() {
            slides.style.transform = `translateX(-${currentIndex * 100}%)`;
            

            dots.forEach((dot, index) => {
                dot.classList.toggle('active', index === currentIndex);
            });
        }

        function changeSlide(direction) {
            currentIndex = (currentIndex + direction + slideElements.length) % slideElements.length;
            updateSlider();
            resetInterval();
        }

        function goToSlide(index) {
            currentIndex = index;
            updateSlider();
            resetInterval();
        }

        function resetInterval() {
            clearInterval(slideInterval);
            startAutoSlide();
        }

        function startAutoSlide() {
            slideInterval = setInterval(() => {
                changeSlide(1);
            }, 3000);
        }

        startAutoSlide();