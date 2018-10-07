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

### *Await* and *Sync*
Await and sync can resolve above issues in a more elegant way. So, let's look at these two keywords: await and sync


### Async functions

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
The keyword await makes JavaScript wait until that promise settles and returns its result (no matter is resolve() or reject()). It works only inside async functions.


```Javascript
async function f() {

  /* Create a promise here that will resolve in 2 seconds */
  let promise = new Promise((resolve, reject) => {
    setTimeout(() => resolve("done!"), 2000)
  });

  let result = await promise; // wait till the promise resolves (*)

  console.log(result); // "done!"
}

f(); // It will print the result after 2 seconds
```
