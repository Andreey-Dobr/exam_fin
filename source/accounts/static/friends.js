async function addFriends(event) {
    event.preventDefault();
    let friendBtn = event.target;
    console.log(friendBtn)
    let url = friendBtn.href;
    console.log(url)
    try {
        let response = await makeRequest(url, 'POST');
        console.log(response);
        let data = await response.text();
        console.log(data);
        counter.innerText = data;
    }
    catch (error) {
        console.log(error);
    }

}


window.addEventListener('load', function() {
    const friendButtons = document.getElementsByClassName('add');
    console.log(friendButtons)
    for (let btn of friendButtons) {btn.onclick = addFriends}

});