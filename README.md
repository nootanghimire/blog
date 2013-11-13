The Static Blog
====

This thing helps me generate my blog. I generally write html files for my blog, This tool only helps me create files and folder structures, Nothing more.


The Process
===

I've defined a `site.template` file which contains a basic template (the part of html after title tag, and upto the top content).

To add a new post: Run the `newPost.py` command (designed for python3). It is interactive. It asks if we want to enter a custom time or not.

[[ScreenShot]]

The scripts automatically creates necessary folders according to the date. And then it asks for the title of the post. 

[[ScreenShot]]

After entering the title, it mades it file-name-friendly (replace space with dash, and strip spaces), and creates the file in appropriate folder, and opens up the directory using nautilus.

