// import * as api from "../api.js";
//
// // Implement application-specific request
//
// async function getAllCategories() {
//     return await api.get('/api/router/category/')
// }
//
// async function getCategoryById(id) {
//     return await api.get('/api/router/category/' + id)
// }
//
// async function createCategory(data) {
//     return await api.post('/api/router/category/', data)
// }
//
// async function editCategory(id, data) {
//     return await api.put('/api/router/category/' + id, data)
// }
//
// async function patchCategory(id, data) {
//     return await api.patch('/api/router/category/' + id, data)
// }
//
// async function deleteCategory(id) {
//     return await api.del('/api/router/category/' + id)
// }
//
// async function searchCategory(query) {
//     return await api.get(`/api/router/category/?search=${query}`)
// }
//
// export {
//     getAllCategories,
//     getCategoryById,
//     createCategory,
//     editCategory,
//     patchCategory,
//     deleteCategory,
//     searchCategory,
// }