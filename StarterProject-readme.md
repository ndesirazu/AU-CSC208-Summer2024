# Getting Started with Python and GitHub

## Objective:

In this project, you will complete several tasks to demonstrate your readiness for the course. By the end of the project, you will have:
1. Created a GitHub account and associated it with your american.edu email address.
2. Installed Git on your computer.
3. Gained basic knowledge of the command-line interface (CLI) for your operating system.
4. Confirmed that you have Python 3.x installed and are using the correct version.
5. Downloaded and set up a suitable Integrated Development Environment (IDE).
6. Cloned the project repository locally to your computer.
7. Corrected syntax and logic errors in the starter code to pass all the provided tests.
8. Committed and pushed your changes back to GitHub for grading.

## Step 1 - Create a GitHub account
Go to the [GitHub website](https://github.com) and create an account. They have [student packs](https://education.github.com/pack) that give you access to many things that would otherwise be very expensive, so I recommend you sign up using your `american.edu` email address. You can associate a GitHub account with multiple email addresses.

**Deliverable:** None required for this step, but you must complete this step before you can complete Step 2.

## Step 2 - Get git
1. Visit the Git [website](https://git-scm.com/downloads) and download the latest Git release for your operating system.
2. Install it, using default settings.
3. As a reference for how to use git, I suggest [Coding Domain](http://codingdomain.com/git/), as it avoids some of the more complicated theory behind git and focuses on the bare minimum practicalities. There are also many good videos, but we will go over some basics in class.

**Deliverable:** Update the `responses.md` file with your name and newly obtained GitHub profile name.

## Step 3 - Become familiar with the CLI for your OS

Each Operating System (OS) has at least one primary interface for navigating the system through the command line. These are powerful applications, and allow you to install programs and software libraries or run the programs that you will develop in this course. Every developer should have at least a rudimentary knowledge of how to use the command line application on your system. There are fairly decent introductory videos for how to use the command line options. Many of the commands for both systems are the same (e.g., `cd`, `cat`, `ls`, `python`) but there will be some differences in presentation and overall capability. At this point, you do not need to become a master of your CLI, but a working knowledge of the basic commands is essential. A general overview and history of CLIs can be found in [Keyboards & Command Line Interfaces: Crash Course Computer Science #22](https://www.youtube.com/watch?v=4RPtJ9UyHS0&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo&index=24).

- On macOS, this application is called **Terminal**. [Absolute BEGINNER Guide to the macOS Terminal
  ](https://www.youtube.com/watch?v=aKRYQsKR46I)
- On Windows, this application is called **Powershell**. [Basic Powershell Commands For Beginners](https://www.youtube.com/watch?v=j9wtAezZ9x0). Windows also has the Command Prompt, which is simpler but a bit less powerful. It also shares fewer commands with the terminal on macOS/Linux. But, if the Powershell interface proves overwhelming, it's always an option. I recommend learning one of them well, but you do not need to know both (especially at this point) [Windows Command Line Tutorial - 1 - Introduction to the Command Prompt](https://www.youtube.com/watch?v=MBBWVgE0ewk). 

> Note, understanding how a CLI work relies on you first understanding files and the file system of a desktop computer. If you are unfamiliar with how the file system of your OS operates, you may want to back up and check out some information on file formats and organization. I recommend Crash Course, such as this excellent video on [Files & File Systems: Crash Course Computer Science #20](https://www.youtube.com/watch?v=KN8YgJnShPM&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo&index=21).
 
**Deliverable:** Answer the CLI-related questions in the `responses.md` file 

## Step 4 - Demonstrate you have Python installed. 
Python is an active and evolving language - new versions are released frequently. This course uses the most recent version of Python 3.x. You can easily obtain [Python](https://www.python.org/downloads/) all by itself, or install it as part of a larger collection of useful modules. One of the most popular is [Anaconda](https://www.anaconda.com/products/distribution), which includes a massive assortment of libraries that can be useful for data science but takes up a lot of space on your computer.

Whatever you do, **do not** install a version of Python 2.x for this course. There are huge differences between them, and none of the examples in class or in the book(s) will line up with 2.x. Assignments will also not be accepted if they are submitted using 2.x syntax.

Typing `python --version` into your CLI verifies that you have done this successfully. Here is correct output for an older version that was popular around 2002: 

```terminal 
Python 2.2.2
```

**Deliverable:** Record the output of `python --version` in the `responses.md` file.

## Step 5 - Download and install an IDE
As we discussed in class, you should download and install a powerful IDE or text editor. An IDE will make it easier to perform many coding tasks, but they are more complex applications, and it will be more challenging to become familiar with all the features. There is also a risk that developing all your code in an IDE may make it more challenging to learn the details of writing code on your own - many automated processes that will not always be available in exams or technical interviews.

In this course, you will utilize an Integrated Development Environment (IDE) to write code. While many IDEs exist, examples and in-class support videos will utilize [PyCharm by Jetbrains](https://www.jetbrains.com/). It is freely available to students through an academic license and supports all the software development features that we will use in this course. It is not sufficient to develop your code in this course through the command line or through an online notebook environment (e.g., Jupyter).

**Deliverable:** In this directory, save a screenshot image (e.g., a .jpeg or .png file) showing your installed IDE or text editor open. You can drag and drop the icon for the picture directly into the project view showing all the files - a popup window will ask you if you want to **add the file to the repository**. You should add it to the repository. If you do not know how to take a screenshot on your computer, then learn how from the PCMag article ["How to Take a Screenshot on Any Device"](https://www.pcmag.com/news/how-to-take-a-screenshot-on-any-device). Then modify the responses.md file to indicate which IDE you are using.

## Step 6 - Clone your Repo locally

Because you can see these instructions, that means that you have already followed the link and accepted the assignment. GitHub classroom has automatically created a repository for you on GitHub and imported the starting code into it. You may be reading this in a browser tab or on your phone. For the next steps, you will move this project onto your computer so that you can write and edit code in your IDE. 
1. On this page (GitHub), there is a green big button labeled Code. If you click it, you get the web URL for this online repo. Copy it to the clipboard. 
2. Open PyCharm. Do one of the following:
    - If this is your first PyCharm project, you will see a welcome screen that asks you if you want a `New Project`, `Open`, or `Get from VCS`. Click **Get from VCS**.
    - However, if you have an existing PyCharm project open, click `VCS > Get from Version Control` in the top menu. 
    - Or, if you have an existing PyCharm project that is open and is connected to a Git repo (less likely), click `Git > Clone` in the top menu. 
3. In the window that pops up in PyCharm, there is an empty box labelled URL. Paste the URL you copied from GitHub's big green Code button.
4. Click the Clone button at the bottom of the popup window.
5. If this is your first time cloning a GitHub repository using PyCharm, it will ask you to log in to GitHub, but it will give you options. As of Fall 2023, the security setup requires you to use a "token" generated by GitHub. Please click **use token**, do not click **log in**. This opens a window for you to paste in the token. There's a button to the right that says "generate token" that will take you to GitHub and the token creation screen. Leave all the options alone except for the expiration date at the top - give yourself enough time to finish the semester at least. Accept the options, and a string of characters will appear - copy and paste this back into the PyCharm window and you should be good to go. Make sure you do this as soon as the string is shown to you - if you leave or refresh the page, it will not be shown again.
6. Mark the /src and /test directories as "Sources Root" and "Test Sources Root," respectively. The easiest way to do this is by right-clicking on them and choosing these from the "Mark Directory as..." option. 

**Deliverable:** None required for this step.

## Step 7 - Correct Errors

### Syntax Errors

You should also see a simple - but definitely broken - program in the `/src` directory. How do you know it's broken? Well, a couple of ways. _Syntax errors_ should stand out due to the red underline in your code editor window. Placing the mouse pointer over the error should give you some insight into what is wrong with the code and potentially how to fix it. Using your existing knowledge of the language, correct the syntax errors. 

### Logic Errors

Your code compiles, but how can you be sure that it does what it is supposed to be doing? We use **test cases**. These test cases provide instant feedback that your system runs appropriately and provides the right output for a given input. These tests are included in the test directory, and they follow a pretty straightforward pattern. Each file tests a different method in the starter program, and contains multiple static methods to test the program in a different way. A test method is declared as void, then it sets up a simple version of the problem you are asked to solve. In the example below, the test runs the `addTwoNumbers` method in the `HelloWorld` class and checks that the program does in fact return 2. It does that using `assertEquals`, which is a special _unit test_ command for testing that the results of a method are what we believe they should be. 

Tests can be run by right-clicking the test file and selecting `Run` from the popup menu. Alternatively, you can run all test at once by right-clicking on the test directory and clicking `Run All Tests` from the popup menu. Once you have corrected all the syntax errors, you will have left some logic errors in the code - methods are not returning what is expected. If you run all tests, many tests are failing, and the IDE will tell you what was expected and what was actually returned from the method called in each test.

Throughout this class the starter code that you are given in assignments will contain many test files. As you build the code, the test will give you feedback on whether your solution is logically correct or not. In some projects, you will also experiment with creating test cases of your own, but for now **do not alter** the files in the test directory. 

You will know that you are done fixing syntax and logic errors when all tests pass successfully.

> The testing component of this project is far easier to accomplish using an IDE like the suggested PyCharm. While it is possible to get the tests running without it, it is not recommended and neither the TA nor the Instructors will necessarily be able to help you if you use an alternative method. 

> A handful of students have reported issues getting the tests to run. Some version of "tests not found" or even more cryptic feedback from PyCharm. For some reason, those student's version of PyCharm / Python decided to use "nose" as a testing framework. The tests were written for a framework called pytest, which is usually the default testing framework installed with python. Take a look at the [documentation page](https://www.jetbrains.com/help/pycharm/testing-frameworks.htmlLinks) for PyCharm to determine if your PyCharm is trying to use nose. The link also shows how to switch it over to pytest - there's even a helpful "fix me" button if pytest is not available in your interpreter. .

**Deliverable:** All tests must pass.

## Step 8 - Update your local repo and push to GitHub

Once you have the code where you want it, correcting as many logical and syntax errors as you can, you need to submit it back to us for grading through GitHub. The easiest way to do this is directly through PyCharm. 

1. In the Git top menu you will find the `commit` option. Depending on the layout of PyCharm on your machine, you may also see on the menu bar of icons next to the `run` command is a green check mark. Clicking this icon or choosing Git > Commit initiates a `commit`. A window will pop up. Enter a meaningful comment in the text box to indicate your progress so far. These are useful for us to understand what's working and what's not. Once you have a good message, click the `commit` button on the bottom. After a commit, you have effectively saved a local backup. Commit as many changes as you want - these are useful in case you really mess something up and need to go back to a working version of the code (we will discuss later in class how to restore these backups). But, your instructor does not have access to these commits until you `push` them.
2. In the Git top menu you will also find the `push` option. As with the check mark, on some PyCharm layouts you will also find next to the check mark a green arrow that points up and to the right. Clicking this icon or choosing Git > Push initiates a `push`. Another window will pop up, asking if you want to push any/all commits that you have made but have not yet pushed. For this project, this will be pretty simple - just click `push`. This will push committed changes from your local repository back to GitHub. Now your instructor and TA can see them.

Alternatively, you can commit and push your changes directly through the CLI:

1. `git add .` This command will stage the changes you have made to the local repository and add any new files to the repo.
2. `git commit -m replace_with_commit_message_in_quotes` This will commit staged changes to your local repository. Make sure to change the _commit_message_ to some meaningful reminder about the changes you have made.
3. `git push` This will push committed changes from your local repository back to GitHub. Now your instructor and TA can see them.

You should get used to using these commands frequently. Much of the challenge of developing complex software is learning to read error messages and feedback from the command line. If you type the command `git status` the command line will print out the current status of the repo. This will usually give you a clue for what you need to do next.

> All changes to your files should be made to your local computer, then committed/pushed to the web. While GitHub does give you the ability to directly edit certain files through the browser, you SHOULD NOT edit them in this way. I know it can be tempting for little changes like to the responses.md. But this can create synchronization problems with your local copy, which will no longer want to push to the web page. It's all very fixable, but confusing at this stage for you. So don't do it!


**Deliverable:** Push the corrected project code back to the online repository. When you are satisfied and think your work is done, let us know on Canvas by typing "DONE" into the text box. This will let us know your submission is ready to grade.

# Grading
Please refer to the learning management system (LMS) for the assignment grading rubric. 

# Getting Stuck
There are times when you might get stuck on some part of an assignment. It happens to the best of us. If you need assistance on a specific part of your code, then be sure to try to `commit` AND `push` the most recent version of your files to GitHub. It makes it much easier for your instructor and TA to provide specific feedback on individual lines of code in the files that you submit. 

# Documenting your Work
Regardless of the method of pushing changes to the server, you will need to become familiar with a very common cycle of making changes to your local repository then pushing those changes back to GitHub where your instructor can review them and assign grades. When you save them through your IDE, this saves a copy of the changes you have made to your system, but have not saved them to your local repository or made them available online to us.

As demonstrated in class, you should make a habit of saving your work incrementally to GitHub. Do not treat submission as a one-time thing. Instead, think of it like a backup. If your laptop gets destroyed, GitHub will still have a copy of your latest pushed commits. This habit of frequent commits also provides us with evidence that all of the code that you submit for this course is your own. 
