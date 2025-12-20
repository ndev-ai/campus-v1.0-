// DOM Elements
const gradientOrb = document.getElementById('gradientOrb');
const nav = document.getElementById('nav');
const heroStats = document.getElementById('heroStats');

// State
let countersVisible = false;

// Initialize
document.addEventListener('DOMContentLoaded', function() {
    setupEventListeners();
    setupIntersectionObserver();
});

// Event Listeners
function setupEventListeners() {
    // Scroll event
    window.addEventListener('scroll', handleScroll);

    // Mouse move for gradient orb
    window.addEventListener('mousemove', handleMouseMove);
}

// Handle scroll
function handleScroll() {
    const scrollY = window.scrollY;

    if (scrollY > 50) {
        nav.classList.add('scrolled');
    } else {
        nav.classList.remove('scrolled');
    }
}

// Handle mouse move
function handleMouseMove(e) {
    if (gradientOrb) {
        gradientOrb.style.left = (e.clientX - 300) + 'px';
        gradientOrb.style.top = (e.clientY - 300) + 'px';
    }
}

// Setup Intersection Observer for counter animation
function setupIntersectionObserver() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !countersVisible) {
                countersVisible = true;
                animateCounters();
            }
        });
    }, { threshold: 0.3 });

    if (heroStats) {
        observer.observe(heroStats);
    }
}

// Animate counters
function animateCounters() {
    const targets = [47, 12, 89, 2.3];
    const duration = 2000;
    const steps = 60;
    const interval = duration / steps;

    let step = 0;
    const timer = setInterval(() => {
        step++;
        const animatedNumbers = targets.map(target =>
            Math.min(target, (target / steps) * step)
        );

        const stat0 = document.getElementById('stat0');
        const stat1 = document.getElementById('stat1');
        const stat2 = document.getElementById('stat2');
        const stat3 = document.getElementById('stat3');

        if (stat0) stat0.textContent = Math.round(animatedNumbers[0]) + '%';
        if (stat1) stat1.textContent = Math.round(animatedNumbers[1]) + 'K+';
        if (stat2) stat2.textContent = Math.round(animatedNumbers[2]);
        if (stat3) stat3.textContent = animatedNumbers[3].toFixed(1) + 'M';

        if (step >= steps) {
            clearInterval(timer);
        }
    }, interval);
}
