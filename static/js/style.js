// ============================================================
// 1. SAHIFA TO‘LIQ YUKLANGANDA ISHGA TUSHADI
// ============================================================
document.addEventListener('DOMContentLoaded', function() {

    console.log('🚀 Sayt ishga tushdi!');

    // ============================================================
    // 2. NAVIGATSIYA LINKLARIGA INTERAKTIV EFFEKTLAR
    // ============================================================
    const navLinks = document.querySelectorAll('nav a');

    navLinks.forEach(link => {
        // Sichqoncha ustiga kelganda
        link.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-3px) scale(1.05)';
            this.style.transition = 'all 0.3s ease';
        });

        // Sichqoncha ketganda
        link.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });

        // Bosilganda (click)
        link.addEventListener('click', function(e) {
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 150);
        });
    });

    // ============================================================
    // 3. KARTALARGA HOVER EFFEKTLAR (qo'shimcha)
    // ============================================================
    const cards = document.querySelectorAll('.card');

    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.borderLeftColor = '#fdcb6e';
            this.style.transition = 'border-left-color 0.4s ease';
        });

        card.addEventListener('mouseleave', function() {
            this.style.borderLeftColor = '#6c5ce7';
        });
    });

    // ============================================================
    // 4. QIDIRUV INPUTIGA AUTOFOCUS (agar mavjud bo'lsa)
    // ============================================================
    const searchInput = document.querySelector('input[name="nom"]');
    if (searchInput) {
        // Sahifa yuklanganda fokus
        searchInput.focus();

        // Tozalash tugmasi (ESC bosganda)
        searchInput.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                this.value = '';
                this.blur();
            }
        });

        // Qidiruv tugmasi (Enter bosganda)
        searchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                this.closest('form').submit();
            }
        });
    }

    // ============================================================
    // 5. FORMA VALIDATSIYASI (maqola yaratish)
    // ============================================================
    const forms = document.querySelectorAll('form');

    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const inputs = this.querySelectorAll('input[required], textarea[required]');
            let isValid = true;

            inputs.forEach(input => {
                if (!input.value.trim()) {
                    isValid = false;
                    input.style.borderColor = '#e94560';
                    input.style.boxShadow = '0 0 0 4px rgba(233, 69, 96, 0.2)';

                    // Xatolik xabari
                    const errorMsg = document.createElement('small');
                    errorMsg.textContent = '⚠️ Bu maydon majburiy!';
                    errorMsg.style.color = '#e94560';
                    errorMsg.style.display = 'block';
                    errorMsg.style.marginTop = '-12px';
                    errorMsg.style.marginBottom = '12px';

                    // Agar xatolik xabari mavjud bo'lmasa
                    if (!input.nextElementSibling || input.nextElementSibling.tagName !== 'SMALL') {
                        input.parentNode.insertBefore(errorMsg, input.nextSibling);
                    }

                    input.addEventListener('input', function() {
                        this.style.borderColor = '';
                        this.style.boxShadow = '';
                        if (this.nextElementSibling && this.nextElementSibling.tagName === 'SMALL') {
                            this.nextElementSibling.remove();
                        }
                    });
                }
            });

            if (!isValid) {
                e.preventDefault();
            }
        });
    });

    // ============================================================
    // 6. SAHIFA YUQORISIGA QAYTISH TUGMASI (agar mavjud bo'lsa)
    // ============================================================
    const backToTop = document.createElement('button');
    backToTop.innerHTML = '⬆';
    backToTop.style.position = 'fixed';
    backToTop.style.bottom = '30px';
    backToTop.style.right = '30px';
    backToTop.style.width = '50px';
    backToTop.style.height = '50px';
    backToTop.style.borderRadius = '50%';
    backToTop.style.background = 'linear-gradient(135deg, #6c5ce7, #a29bfe)';
    backToTop.style.color = 'white';
    backToTop.style.border = 'none';
    backToTop.style.fontSize = '24px';
    backToTop.style.cursor = 'pointer';
    backToTop.style.boxShadow = '0 8px 25px rgba(108, 92, 231, 0.4)';
    backToTop.style.transition = 'all 0.3s ease';
    backToTop.style.opacity = '0';
    backToTop.style.visibility = 'hidden';
    backToTop.style.zIndex = '1000';

    backToTop.addEventListener('click', function() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    backToTop.addEventListener('mouseenter', function() {
        this.style.transform = 'scale(1.1)';
    });

    backToTop.addEventListener('mouseleave', function() {
        this.style.transform = 'scale(1)';
    });

    document.body.appendChild(backToTop);

    // Skroll qilinganda tugmani ko'rsatish
    window.addEventListener('scroll', function() {
        if (window.scrollY > 300) {
            backToTop.style.opacity = '1';
            backToTop.style.visibility = 'visible';
        } else {
            backToTop.style.opacity = '0';
            backToTop.style.visibility = 'hidden';
        }
    });

    // ============================================================
    // 7. KONSOLDA QISQA MA'LUMOT
    // ============================================================
    console.log('📌 Sayt interaktiv qismlari ishga tushdi!');
    console.log('📌 Muallif: Siz');
    console.log('📌 Django loyihasi');
});