// Illustration of the creating and use of functions


function exampleFunction(value1, value2)
{
    var result = value1 * value2;

    return result;
}


var first = prompt("Enter a number: ")

var second = prompt("Enter a second number: ")


console.log("The product of " + first + " and " + second + " is " + exampleFunction(first, second))
// or in a browser
document.write("The product of " + first + " and " + second + " is " + exampleFunction(first, second))

