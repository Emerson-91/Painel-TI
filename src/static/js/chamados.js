document.addEventListener('DOMContentLoaded', function () {
    console.log("JavaScript carregado");
    const rows = document.querySelectorAll('#chamadosTableBody tr');
    const now = new Date().getTime();
    const thirtyMinutes = 30 * 60 * 1000; // 30 minutos em milissegundos

    rows.forEach(row => {
        const criadoEm = parseInt(row.getAttribute('data-criado-em')) * 1000; // Converter para milissegundos
        const timeElapsed = now - criadoEm;

        if (timeElapsed > thirtyMinutes) {
            row.classList.add('blink');
        }
    });
});
