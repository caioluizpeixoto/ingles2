with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace R$17,90 with R$10,00
content = content.replace('R$17,90', 'R$10,00')
content = content.replace('17,90', '10,00')

# Restore the 27,90 string just in case it got affected (though it shouldn't)
# We don't need to, because 27,90 doesn't match 17,90.

# Replace the original button
btn_original = '<a href="https://pay.wiapy.com/58WtAgb6G-T" class="btn-pop mt-8 w-full bg-secondary text-secondary-foreground">QUERO O KIT ESSENCIAL</a>'
btn_new = '<a href="#" id="btn-basic-kit" class="btn-pop mt-8 w-full bg-secondary text-secondary-foreground">QUERO O KIT ESSENCIAL</a>'

if btn_original in content:
    content = content.replace(btn_original, btn_new)
else:
    # try replacing the href only
    content = content.replace('href="https://pay.wiapy.com/58WtAgb6G-T"', 'href="#" id="btn-basic-kit"')

popup_html = """
<style>
#upsell-popup {
    display: none;
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0,0,0,0.8);
    z-index: 9999;
    align-items: center;
    justify-content: center;
}
.popup-content {
    background: #fff;
    padding: 30px;
    border-radius: 16px;
    max-width: 500px;
    text-align: center;
    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    margin: 20px;
    font-family: 'Fredoka', 'Nunito', sans-serif;
}
.popup-title {
    font-size: 24px;
    font-weight: 700;
    color: #e63946;
    margin-bottom: 15px;
}
.popup-desc {
    font-size: 18px;
    color: #333;
    margin-bottom: 25px;
}
.btn-yes {
    display: block;
    width: 100%;
    padding: 15px;
    background: #f4a261; /* Using an existing theme color, maybe orange/yellow */
    color: #fff;
    font-weight: bold;
    font-size: 18px;
    border-radius: 9999px; /* Pill shape like other buttons */
    text-decoration: none;
    margin-bottom: 15px;
    box-shadow: 0 4px 0 #d9823f;
    transition: transform 0.1s;
}
.btn-yes:active {
    transform: translateY(4px);
    box-shadow: 0 0 0 #d9823f;
}
.btn-no {
    display: block;
    width: 100%;
    padding: 10px;
    color: #888;
    font-weight: bold;
    font-size: 14px;
    text-decoration: underline;
}
</style>
<div id="upsell-popup">
    <div class="popup-content">
        <div class="popup-title">ESPERE! OFERTA EXCLUSIVA 🎁</div>
        <div class="popup-desc">
            Que tal levar o <b>Kit Completo (Premium)</b> por apenas <b>R$17,90</b>?<br><br>
            Você terá acesso a todos os materiais extras e bônus exclusivos. Essa oferta não aparecerá novamente!
        </div>
        <a href="https://pay.wiapy.com/58WtAgb6G-T" class="btn-yes">SIM! QUERO O KIT COMPLETO POR R$17,90</a>
        <a href="#" id="btn-no-thanks" class="btn-no">Não, obrigado. Quero apenas o kit de R$10,00</a>
    </div>
</div>
<script>
document.addEventListener("DOMContentLoaded", function() {
    var btnBasic = document.getElementById("btn-basic-kit");
    var popup = document.getElementById("upsell-popup");
    var btnNoThanks = document.getElementById("btn-no-thanks");

    if(btnBasic) {
        btnBasic.addEventListener("click", function(e) {
            e.preventDefault();
            popup.style.display = "flex";
        });
    }

    if(btnNoThanks) {
        btnNoThanks.addEventListener("click", function(e) {
            e.preventDefault();
            // TODO: Replace this URL with the actual 10 reais payment link
            alert("Redirecionando para o checkout de R$ 10,00... (Coloque o link real no código)");
            // window.location.href = "LINK_AQUI";
        });
    }
});
</script>
"""

content = content.replace('</body>', popup_html + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
