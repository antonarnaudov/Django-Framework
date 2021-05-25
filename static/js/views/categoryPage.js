import {render, html} from 'https://unpkg.com/lit-html?module';
import {getAllCategories} from "../api/data/categoryData.js";

const main = document.querySelector('main')


const allCategoriesTemplate = (allCategories) => html`
    <div class="display-container">
        ${allCategories['results'].length > 0 ? allCategories['results'].map(categoryTemplate) : html`
            <!-- No articles message -->
            <h3 class="no-articles">No categories yet</h3>`}

    </div>
`


const categoryTemplate = (category) => html`
    <div class="category">

        <!--        <a class="category-link" href="{% url 'category photos' category.category category.id %}">-->
        <a class="category-link" href="#">

            <div class="image">
                <img src="${category['image']}" alt="{{ category.category }}">
                <div class="filter"></div>
                <h3>${category['category']}</h3>
            </div>
        </a>
        <!--        {% if user.groups.all.0.name == 'Creator' %}-->
        <!--        <div class="editor-buttons">-->
        <!--            <a href="{% url 'edit-category' category.id %}">Edit</a>-->
        <!--            <a href="{% url 'delete-category' category.id %}">Delete</a>-->
        <!--        </div>-->
        <!--        {% endif %}-->
    </div>
`

export async function allCategoriesPage() {
    const categories = await getAllCategories()

    console.log(categories)
    render(allCategoriesTemplate(categories), main)
}

await allCategoriesPage()
