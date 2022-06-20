console.log('get data');
fetch(`http://127.0.0.1:5000/notes/all_notes`, {
})
    .then(res => res.json())
    .then(data => {
        value = Object.values(data)
        val = value[0]
        for (i = 0; i < val.length; i++) {
            const id = val[i].id
            const title = val[i].title
            const content = val[i].content
            const html =
            `<div >

            <h3>${title}</h3></br>
            <p style="text-align:center;">${content}</p>
            <button type="button" class="btn btn-danger" value="${id}">Danger</button>

            </div>`
            document.getElementById('response').innerHTML += html

        }
        del_btn = document.getElementsByClassName('btn btn-danger')
            console.log(del_btn)
            for (const delbtn of del_btn) {
                delbtn.addEventListener('click', function() {
                    console.log('delete')
                    fetch(`http://127.0.0.1:5000/notes/delete/${parseInt(delbtn.value)}`, {
                        method: 'DELETE',
                    })
                        .then(res => res.json())
                        .then(data => {
                            console.log(data)
                        })
            })
        }
    })


let btn2 = document.getElementById('add_note');
btn2.addEventListener('click', () => {

    console.log('post data');
    fetch('http://127.0.0.1:5000/notes', {
        headers: {
            'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify({
            title: document.getElementById('title').value,
            content: document.getElementById('content').value
        })
    })
        .then(res => res.json())
        .then(data => {
            console.log(data)
        })
});
