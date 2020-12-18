// Meta tags

meta = document.createElement('meta')
meta.name = "robots"
meta.content = "index, follow"
document.getElementsByTagName('head')[0].appendChild(meta);

meta = document.createElement('meta')
meta.name = "author"
meta.content = "Yuvraj Garg"
document.getElementsByTagName('head')[0].appendChild(meta);

setTimeout(()=>{

    // Meta Tags
    meta_keywords = document.createElement('meta')
    meta_description = document.createElement('meta')
    meta_keywords.name = "keywords"
    meta_description.name = "description"

    console.log("QUANTML")
    // document.querySelectorAll('.streamlit-expanderHeader').forEach(function(element, index){
    //     element.style.borderBottomColor = "rgb(145, 145, 145)";
    //     element.addEventListener("mouseover", function( event ) {
    //         element.style.borderBottomColor = "#0073b1";
    //     })
    //     element.addEventListener('mouseleave', e => {
    //         element.style.borderBottomColor = "rgb(145, 145, 145)";
    //     })
    // })
    // document.querySelectorAll('.streamlit-expanderContent ').forEach(function(element, index){
    //     element.style.borderBottomColor = "rgb(145, 145, 145)";
    // })


    chapter = document.getElementById('quantml-chapter')
    if(chapter == null){

    } else if(chapter.innerHTML == "wlln"){
        // console.log("current chapter: Weak Law of Large Numbers")
        // document.querySelector('title').innerHTML = "Weak Law of Large Numbers | Statistics App - Quantml"
        meta_keywords.content = "statistics,weak law of large numbers,visualization,weak law of large numbers visualization,law of large numbers,law of large numbers visualization,statistics app,quantml"
        meta_description.content = "Visualize Weak Law of Large Numbers | Statistics. See how changing parameters, distribution affects convergence. app.quantml.org here you can learn concepts by interacting with them."
    } else if (chapter.innerHTML == "clt"){
        // console.log("current chapter: Central Limit Theorem")
        // document.querySelector('title').innerHTML = "Central Limit Theorem | Statistics App - Quantml"
        meta_keywords.content = "statistics,central limit theorem,visualization,central limit theorem visualization,statistics app,quantml"
        meta_description.content = "Visualize Central Limit Theorem | Statistics. See how changing parameters, distribution affects convergence. app.quantml.org here you can learn concepts by interacting with them."
    }

    // Adding meta tags
    document.getElementsByTagName('head')[0].appendChild(meta_keywords);
    document.getElementsByTagName('head')[0].appendChild(meta_description);
}, 2000)

// quantmlCreateAttributeDiv("set-quantml-cookie", {name: "theme", value: "light"})

body   = document.querySelector("body")
const observer = new MutationObserver(function(mutations){
    setTimeout(function(){
        document.querySelectorAll("#set-quantml-cookie").forEach(function(element, index){
            document.cookie = `${element.getAttribute("name")}=${element.getAttribute("value")}`
            console.log("Set Cookie")
            element.remove()
        })
    }, 0)
})
observer.observe(body, {
    childList:true,
    subtree:true
})

// div.remove()