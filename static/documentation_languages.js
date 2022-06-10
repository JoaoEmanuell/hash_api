"use strict";
function main() {
    const supported_languages = [
        ['Português', 'pt-br', 'Linguagem'],
        ['English', 'en', 'Language'],
    ];
    const url_treated = window.location.href.split('/');
    if (url_treated[3] == 'docs') {
        const div_translated = document.getElementById('translated');
        // Elements
        const li_base_element = document.createElement('li');
        const a_base_element = document.createElement('a');
        const ul_base_element = document.createElement('ul');
        // a element atributes
        a_base_element.setAttribute('class', 'nav-link dropdown-toggle');
        a_base_element.setAttribute('href', '#');
        a_base_element.setAttribute('id', 'navbarDropdown');
        a_base_element.setAttribute('role', 'button');
        a_base_element.setAttribute('data-bs-toggle', 'dropdown');
        a_base_element.setAttribute('aria-expanded', 'false');
        a_base_element.innerHTML = 'Language';
        li_base_element.className = 'nav-item dropdown';
        // ul element atributes
        ul_base_element.setAttribute('class', 'dropdown-menu');
        ul_base_element.setAttribute('aria-labelledby', 'navbarDropdown');
        // Dropdown Menu
        // Object.entries convert a object to array
        supported_languages.forEach(element => {
            const li_internal_element = document.createElement('li');
            const ul_internal_a_element = document.createElement('a');
            ul_internal_a_element.setAttribute('href', `/docs/?language=${element[1]}`);
            ul_internal_a_element.setAttribute('class', 'dropdown-item');
            ul_internal_a_element.innerHTML = element[0];
            li_internal_element.appendChild(ul_internal_a_element);
            // Append in ul
            ul_base_element.appendChild(li_internal_element);
            // Verify if the language is the last current language
            if (element[1] != supported_languages[supported_languages.length - 1 // Last element
            ][1]) {
                const hr = document.createElement('hr');
                hr.setAttribute('class', 'dropdown-divider');
                ul_base_element.appendChild(hr);
            }
        });
        // Append elements
        li_base_element.appendChild(a_base_element);
        li_base_element.appendChild(ul_base_element);
        div_translated.appendChild(li_base_element);
    }
}
main();
