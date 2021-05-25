import * as api from "../api.js";

// Implement application-specific request

async function getAllPhotos() {
    return await api.get('/api/router/photos/')
}

async function getPhotoById(id) {
    return await api.get('/api/router/photos/' + id)
}

async function createPhoto(data) {
    return await api.post('/api/router/photos/', data)
}

async function editPhoto(id, data) {
    return await api.put('/api/router/photos/' + id, data)
}

async function patchPhoto(id, data) {
    return await api.patch('/api/router/photos/' + id, data)
}

async function deletePhoto(id) {
    return await api.del('/api/router/photos/' + id)
}

async function searchPhotosByName(query) {
    return await api.get(`/api/router/photos/?search=${query}`)
}

async function filterPhotosByPrice(minPrice, maxPrice) {
    if (minPrice && maxPrice){
        return await api.get(`/api/router/photos/?min_price=${minPrice}&max_price=${maxPrice}`)
    } else {
        if (minPrice) {
            return await api.get(`/api/router/photos/?min_price=${minPrice}&max_price=`)
        } else if (maxPrice) {
            return await api.get(`/api/router/photos/?min_price=&max_price=${maxPrice}`)
        }
    }
}

async function orderPhotosByPrice(ascending) {
    if (ascending) {
        return await api.get(`/api/router/photos/?ordering=price`)
    }
    return await api.get(`/api/router/photos/?ordering=-price`)
}

export {
    getAllPhotos,
    getPhotoById,
    createPhoto,
    editPhoto,
    patchPhoto,
    deletePhoto,
    searchPhotosByName,
    filterPhotosByPrice,
    orderPhotosByPrice
}