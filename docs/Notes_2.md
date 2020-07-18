## Module 2

0. Prerequisites
Module-1

1. Mock user template
- replace `Hello, world!` with a dictionary with `{username: USER_NAME}`
- return an in line HTML

2. create the template directory under app
```shell
mkdir -p app/templates
```

3. create the index.html under templates
```shell
touch app/templates/index.html
```

4. add render_template to routes.py and in the return pass the title and the user dictionary created earlier
- can also pass posts and loop through them in the template

5. create the base.html under templates for template inheritance
```shell
touch app/templates/base.html
```
- add a link to the home (index) page and a block content for the body
- add extends to index.html and only leave the block content

Next: [module 03](Notes_3.md)