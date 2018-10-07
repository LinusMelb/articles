### Callback, promise and keywords: Await, sync in JavaScript
#### Linus, 2018/10/07 3pm
#### This article will help you understand
1. what callback function is and how to use it
2. what promise is and how to write promise to handle asynchronous request.
3. await and sync keywords

---

### Callback function
Every function has an optional parameter, callback, that can be passed into the function.


For example, if we want to get all posts after we create a new post, we have to wait until the create operation has been done.
Therefore, we can pass a callback(getPosts) to createPost function that will be execute after the creation.

```Javascript
let posts = [];

createPost(post, callback) {
  setTimeout(() =>{
      posts.push(post);
      /* after post has been created */
      callback();
  }, 2000);
}

getPosts(){
  setTimeout(() =>{
      console.log(posts);
  }, 1000);
}

// We pass getPosts function as callback to createPost
createPost(post, getPosts()); // It will print result after 3 seconds
```

---

### Promise
Before promise we use Callback to handle asynchronous call. But if we'd like to perform the same operations 10 times, we have to nested 10 times, that's so called "callback hell"
Here's an example, if we add 2 numbers every 3 seconds and we do it 3 three times, code in writing callback would be:

```Javascript
// Function to add two numbers every 3 seconds
function addAsync (num1, num2, callback) {
    // add two numbers in 3 seconds
    setTimeout(() => {
      result = num1 + num2;
      // after 3 sec, run callback()
      callback(result);
    }, 3000);
}
// We have to nest same function 3 times
addAsync(1, 2, (result) => {
  addAsync(result, 3, (result2) => {
    addAsync(result2, 4, (result3) => {
      console.log(result3); // print final result in 9 seconds, 1+2+3+4 = 10
    });
  });
});
```


However, we can use promise to deal with it elegantly. One thing to note:
- If a function returns *resolve(result)* promise, we can use **.then()** to catch result
- If a function returns *reject(error)* promise, we can use **.catch()** to deal with the error.

```Javascript
// Function to add two numbers in 3 seconds
function addAsync (num1, num2) {
    let result;
    return new Promise((resolve, reject) => {
    	setTimeout(() => {
    		result = num1 + num2;
        // after 3 sec, resolve the result
    		resolve(result);
      }, 3000);
    });
}

addAsync(1, 2) // returns promise which is resolve(3)
.then((result) => { return addAsync(result, 3); }) // returns promise which is resolve(6)
.then((result1) => { return addAsync(result1, 4); }) // returns promise which is resolve(10)
.then((result2) => { console.log(result2) }); // print 10, total time: 9 seconds
```

---

### *Await* and *Sync*
Await and sync resolves above issues using promise as well. So, let's look at these two keywords: await and sync


### Async functions
The word “async” before a function means one simple thing: *a function always returns a promise*

```Javascript
/* async keyword before a function means the function will always return a promise,
JavaScript automatically wraps it into a resolved promise with that value. */
async function f() {
  return 2018;
}

/* Promise has a feature that we can add .then() after function to handle the response
   In this case, the response is 2018, we pass it to a anonymous function to print it. */
f().then((value) => {
  console.log("The value returned by f() is" + value);
  // output: "The value returned by f() is 2018"
});

```

### Await
The keyword await makes JavaScript wait until that promise settles and returns its result (no matter is resolve() or reject()).
*It works only inside async functions*


```Javascript
async function f() {

  /* Create a promise here that will resolve in 2 seconds */
  let promise = new Promise((resolve, reject) => {
    setTimeout(() => resolve("done!"), 2000)
  });

  let result = await promise; // wait till the promise resolves (*)

  console.log(result); // It will print the result after 2 seconds
}

f();
```
