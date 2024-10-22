// qrcode.js
function generateQRCode(url) {
    const qr = new QRCode(document.getElementById("qr-code"), {
        text: url,
        width: 128,
        height: 128
    });
}

// Obtener la URL del código QR desde el servidor (por ejemplo, a través de una API)
fetch('/get_qr_code')
  .then(response => response.json())
  .then(data => {
    generateQRCode(data.qr_code_url);
  });