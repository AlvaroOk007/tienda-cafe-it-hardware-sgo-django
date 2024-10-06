// Inicializar localStorage si no existe
if (!localStorage.getItem('carrito')) {
    localStorage.setItem('carrito', JSON.stringify([]));
}
