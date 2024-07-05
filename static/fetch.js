document.addEventListener('DOMContentLoaded', () => {
    const contenedorProductos = document.getElementById('contenedor-productos');

    // Función para obtener datos desde la API
    async function obtenerDatos() {
        try {
            const response = await fetch('http://127.0.0.1:5000');
            const data = await response.json();

            data.forEach(tipoProducto => {
                const articulo = document.createElement('div');
                articulo.classList.add('articulo');

                const h1 = document.createElement('h1');
                h1.textContent = tipoProducto.tipo_producto;
                articulo.appendChild(h1);

                const productoContainer = document.createElement('div');
                productoContainer.classList.add('producto-container');

                tipoProducto.productos.forEach(producto => {
                    const productoDiv = document.createElement('div');
                    productoDiv.classList.add('producto');

                    if (producto.imagen_base64) {
                        const img = document.createElement('img');
                        img.src = 'data:image/png;base64,' + producto.imagen_base64;
                        img.alt = producto.tipo_material; // Ajusta según sea necesario
                        productoDiv.appendChild(img);
                    } else {
                        const noImage = document.createElement('p');
                        noImage.textContent = 'Imagen no disponible';
                        productoDiv.appendChild(noImage);
                    }

                    productoContainer.appendChild(productoDiv);
                });

                articulo.appendChild(productoContainer);
                contenedorProductos.appendChild(articulo);
            });
        } catch (error) {
            console.error('Error al obtener los datos:', error);
        }
    }

    obtenerDatos();
});
