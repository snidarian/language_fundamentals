// There are many ways to manipulate the Document Object model in JavaScript

// source of information
// https://www.youtube.com/watch?v=y17RuWkWdn8


// Many if not all these methods involve using the 'document' object that every web browser page contains in order to make changes to the pages html or CSS, or to provide interactivity and so forth. 




// Adding elements to the page
const body = document.body
body.append("This is a string")

// appending elements

const div = document.createElement('div')

body.append(div)

// creating elements

// modifying element text
// Adding text to the element

div.textContent = "This is text inside this div"

body.append(div)


// modifying element HTML
// .innerHTML method can present security concerns (html injection)
div.innerHTML = "<strong>Hello world</strong>"

const strong_text = document.createElement('strong')

strong_text.innerText = 'Hello world'


// modifying element attributes

const body = document.body
const div = document.querySelector("div")
const element0 = document.querySelector("#html_id")
const element1 = document.querySelector("#html_id")

// remove child elements
div.removeChild(element0)


// modifying data attributes

// you can print an elements attributes to the console like this
console.log(element0.getAttribute("id"))
console.log(element0.getAttribute("class"))
console.log(element0.getAttribute("title"))


// you can also remove attributes
element0.removeAttribute("id")


// modifying element classes



