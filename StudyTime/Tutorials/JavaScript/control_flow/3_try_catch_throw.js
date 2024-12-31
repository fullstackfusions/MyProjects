// try - try the code
// catch - handle the error (in python it's `exception`)
// throw - statement lets you make your own error (in python it's `raise`)
// finally - statement lets you execute code after try and catch

// example 1 try catch
try {
    alert("Welcome developers!")
}
catch (err) {
    console.log(err);
}


// example 2 try catch and throw
try {
    throw new Error('Yeah... Sorry')
}
catch (e) {
    console.log(e);
}


// example 3 try catch and finally
try {
    console.log('Trying to check the error...')
}
catch (err) {
    console.log(err);
}
finally {
    console.log('finally block executes regardless of the try catch result')
}