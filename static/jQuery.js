async function sendReq(){
    const res = await axios.post("http://127.0.0.1:5000/start",{"guess":`${userGuess}`})
    console.log(res)
    $("#score").text(`${res.data.Score}`)
    $("body").append(`<p id="result">${res.data.display}</p>`)
}



$("form").on("submit",function(event){
    $("#result").remove()
    event.preventDefault()
    userGuess = $("input[type=text]").val()
    sendReq()

})


