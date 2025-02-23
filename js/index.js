document.addEventListener('DOMContentLoaded', () => {
    const circle = document.querySelector('.neon-circle');
    const shapes = document.querySelectorAll('.neon-shape');

    // Animate the circle
    circle.animate([
        {opacity: 0.5}
        { transform: 'translateX(-50%) translateY(0)' },
        { transform: 'translateX(-50%) translateY(-30%)' }
    ], {
        duration: 8000,
        iterations: Infinity,
        direction: 'alternate',
        easing: 'ease-in-out'
    });

    // Animate all shapes
    shapes.forEach(shape => {
        shape.animate([
            { opacity: 0.3, filter: 'blur(5px)' },
            { opacity: 0.5, filter: 'blur(3px)' }
        ], {
            duration: 4000,
            iterations: Infinity,
            direction: 'alternate',
            easing: 'ease-in-out'
        });
    });
});