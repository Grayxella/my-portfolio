function toggleMenu() {
    document.getElementById("navLinks").classList.toggle("show");
}
document.getElementById("year").textContent = new Date().getFullYear();
document.querySelectorAll("#navLinks a").forEach(link => {
    link.addEventListener("click", () => {
        document.getElementById("navLinks").classList.remove("show");
    });
});