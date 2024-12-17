const titleInput = document.querySelector('input[name=title]');
const slugInput = document.querySelector('input[name=slug]');

/* trim any white space
/* /&/g replace & "/g" globally with -and-
   second replace using regular expressions */
const slugify = (val) => {
  return val.toString().toLowerCase().trim()
  .replace(/&/g, '-and-')    // replace & with -and-
  .replace(/[\s\W-]+/g, '-') // replace spaces, non-word char & dashes with -
};

/* add event listener
(e) take the event (an arrow function)*/
titleInput.addEventListener('keyup', (e) => {
  slugInput.setAttribute('value', slugify(titleInput.value));
});
