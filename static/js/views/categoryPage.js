// import {render, html} from 'https://unpkg.com/lit-html?module';
// import {deleteCategory, getAllCategories} from "../api/data/categoryData.js";
// import {getUserData} from "../api/data/userData.js";
//
// const main = document.querySelector('main')
//
//
// const allCategoriesTemplate = (allCategories, user) => html`
//     <div class="display-container">
//         ${allCategories['results'].length > 0 ?
//                 allCategories['results'].map(category =>
//                         categoryTemplate(category, user)) : html`
//                     <!-- No articles message -->
//                     <h3 class="no-articles">No categories yet</h3>`}
//
//     </div>
// `
//
//
// const categoryTemplate = (category, user) => html`
//     <div class="category">
//
//         <a class="category-link" href="/${category['category']}/${category['id']}/photos">
//
//             <div class="image">
//                 <img src="${category['image']}" alt="{{ category.category }}">
//                 <div class="filter"></div>
//                 <h3>${category['category']}</h3>
//             </div>
//         </a>
//
//
//     </div>
// `
//
// export async function allCategoriesPage() {
//     const categories = await getAllCategories()
//     const user = await getUserData()
//
//     render(allCategoriesTemplate(categories, user), main)
// }
//
// await allCategoriesPage()

// `
//         ${user['groups'][0] === 1 ? html `
//             <div class="editor-buttons">
//                 <a href="category/edit/${category['id']}/">Edit</a>
//                 <a @click=${helpers.deleteCategory(category['id'])} href="javascript:void(0)">Delete</a>
//             </div>
//         ` : ''}
// `