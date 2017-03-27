# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > pwd                                                                                   - show current working directory path
mkdir                                                                                 - creating a directory
rmdir                                                                                 - deleting a directory
touch filename                                                                    - creating a file using touch command
rm filename                                                                       - deleting a file
mv oldfilename newfilename                                            - renaming a file
ls -a                                                                                    - listing hidden files
mv oldDir/oldfilenme newDir/newfilename                     - copying a file from one directory to another
find . -name "filename" -print                                           - find a file
help                                                                                    - gets command line help

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > `ls`                      - list contents of current directory  
`ls -a`                  - list contents of current directory including hidden contents
`ls -l`                  - list contents of current directory including permissions
`ls -lh`                 - list contents of current directory including permissions
`ls -lah`                - list contents of current directory including permissions including hidden files
`ls -t`                   - list contents of current directory with newest files first
`ls -Glp`              - list contents of current directory  with permissions

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > ls -m 	Displays the names as a comma-separated list, ls -d Displays only directories, ls -1 	Displays each entry on a line, ls -c	Displays files by file timestamp, ls -C	Displays files in a columnar format (default)

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > `xargs` are commands that allow one to construct complex commands for commandline commands.  Here is an example from Wikipedia where xargs are used to find a file path: `find /path -type f -print | xargs rm`
 

