import * as api from "../api.js";

// Implement application-specific request

async function getAllCartItems() {
    return await api.get('/api/router/cart/')
}

async function getCartItemById(id) {
    return await api.get('/api/router/cart/' + id)
}

async function addToCart(data) {
    return await api.post('/api/router/cart/', data)
}

async function removeFromCart(id) {
    return await api.del('/api/router/cart/' + id)
}

async function searchPhotoInCart(query) {
    return await api.get(`/api/router/cart/?search=${query}`)
}

export {
    getAllCartItems,
    getCartItemById,
    addToCart,
    removeFromCart,
    searchPhotoInCart,
}