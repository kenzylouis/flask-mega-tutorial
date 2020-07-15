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
