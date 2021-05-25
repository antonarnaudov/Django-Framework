// Set the server host address
const settings = {
    host: 'http://127.0.0.1:8000',
    // host: 'http://localhost:8000',

}

async function request(url, options) {
    try {
        const address = settings.host + url
        const response = await fetch(address, options)

        if (response.ok === false) {
            if (response.status === 500) {
                throw new Error('No user logged in.')
            }
            const error = await response.json()
            throw new Error(error.message)
        }

        try {
            return await response.json()
        } catch (error) {
            return response
        }

    } catch (err) {
        if (err.message) {
            alert(err.message)
        }
        // Throw prevents returning undefined
        throw err;
    }
}

function getOptions(method = 'get', body) {
    const options = {
        method,
        headers: {},
    }

    const csrftoken = getCookie('csrftoken')
    if (csrftoken !== null) {
        options.headers['X-CSRFToken'] = csrftoken
    }

    if (body) {
        options.headers['Content-Type'] = 'application/json'
        options.body = JSON.stringify(body)
    }
    return options
}

function getCookie(name) {
    let cookieValue;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

async function get(url) {
    return await request(url, getOptions())
}

async function post(url, data) {
    return await request(url, getOptions('post', data))
}

async function put(url, data) {
    return await request(url, getOptions('put', data))
}

async function patch(url, data) {
    return await request(url, getOptions('patch', data))
}

async function del(url) {
    return await request(url, getOptions('delete'))
}

// async function login(email, password) {
//     const result = await post('/users/login', { email, password })
//
//     sessionStorage.setItem('email', result.email)
//     sessionStorage.setItem('authToken', result.accessToken)
//     sessionStorage.setItem('userId', result._id)
//
//     return result
// }
//
// async function register(email, password) {
//     const result = await post('/users/register', { email, password })
//
//     sessionStorage.setItem('email', result.email)
//     sessionStorage.setItem('authToken', result.accessToken)
//     sessionStorage.setItem('userId', result._id)
//
//     return result
// }
//
// async function logout() {
//     const result = await get('/users/logout')
//
//     sessionStorage.removeItem('email', result.email)
//     sessionStorage.removeItem('authToken', result.accessToken)
//     sessionStorage.removeItem('userId', result._id)
//
//     return result
// }

export {
    get,
    post,
    put,
    patch,
    del,
}
