### Await, sync, callback and promises in JavaScript
#### Linus, 2018/10/07 3pm
#### Javascript promise is an important feature. It helps handle asynchronous request. Therefore, I would like to write down the way I understand promises.

---

### *Await* and *Sync*
At first, Let me talk about the 2 keywords: await and sync


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
