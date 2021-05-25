import * as api from "../api.js";

// Implement application-specific request

async function getAllWishes() {
    return await api.get('/api/router/wishes/')
}

async function getWishById(id) {
    try {
        await api.get('/api/router/wishes/' + id)
        return true
    } catch (err) {
        return false
    }
}

async function addToWishlist(data) {
    return await api.post('/api/router/wishes/', data)
}

async function removeFromWishlist(id) {
    return await api.del('/api/router/wishes/' + id)
}

async function searchPhotoInWishlist(query) {
    return await api.get(`/api/router/wishes/?search=${query}`)
}

export {
    getAllWishes,
    getWishById,
    addToWishlist,
    removeFromWishlist,
    searchPhotoInWishlist,
}