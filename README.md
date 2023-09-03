<img width="150" align="right" src="./resources/scraping_logo.png" alt_text="[https://www.flaticon.com/free-icons/scraping](https://www.flaticon.com/free-icons/scraping)"></img>

# University notices email notifier
<p align="justify">Scraper for notices on <a href="https://efee.etf.unibl.org/oglasi/">Faculty of Electrical Engineering Banja Luka</a> website. Project scrapes notices from a website and after ETL processing data is sent to the appointed email address through Yahoo SMTP, using <a href="https://docs.python.org/3/library/smtplib.html">smtplib</a> library, in a form of a JSON file.</p>

## Table of contents
- [University notices email notifier](#university-notices-email-notifier)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Initial Setup](#initial-setup)
  - [Config file setup](#config-file-setup)
    - [Yahoo SMTP](#yahoo-smtp)
  - [Scheduling scraping](#scheduling-scraping)
    - [Windows - Task Scheduler](#windows---task-scheduler)
    - [Linux - Cron job](#linux---cron-job)
  - [To-Do List](#to-do-list)

## Introduction
<p align="justify">I've always wanted to build a web scraper and recently I found some free time recently to complete this project. Because the website is dynamic, scraping was done with <a href="https://selenium-python.readthedocs.io/api.html">Selenium API</a> in addition to <a href="https://pypi.org/project/beautifulsoup4/">Beautiful Soup</a> library. The project is written in such way that it can be run both on Windows and Linux.</p>

> **Note**:
> <ul><li>In order for any of this to work one prerequisite is that you have installed Python 3 on your machine.</li>
> <li>Be cautious when changing <i>config.ini</i> because it's tightly coupled with python code.</li>
> <li>The code is tested both on Windows 10 and latest Linux Mint distribution.</li></ul>

## Initial Setup
<p align="justify">In this section I will go over details how to setup this project on Linux. However, majority of the steps are also applicable on Windows. Firstly you will open the Command line and position yourself to the desired directory, after which you will need to clone this repository using <code>git clone</code> command.</p>

```
$ git clone https://github.com/AleksaMCode/university-notices-email-notifier.git
```

<p align="justify">Next, position yourself inside of the project directory, create a virtualenv and then install all of the needed packages from the <i>requirements.txt</i> file.</p>

```shell
$ cd university-notices-email-notifier
$ virtuelenv venv
$ virtualenv venv --distribute
$ source venv/bin/activate
(venv) pip install -r requirements.txt
```

> **Note**: <br>
> <p align="justify">All of these commands you can find in <i>init.sh</i> file that is located inside of the <i>resources/scripts</i> directory.</p>


## Config file setup
<p align="justify">Before using this project you first need to adjust a couple of parameters stored in a config ini file. Firstly you'll need to add an email address (<i>user_email</i> field) you wish to use to receive the email notification. If you wish to use Yahoo SMTP, you only need to update the <i>email</i> and <i>password</i> fields with your own credentials. Below you can find detail instruction how to set up Yahoo SMTP with your account. If for some reason you want to use another email provider, then you will need, in addition to the previously mentioned fields, to update fields that are provider specific, such as <i>port</i> and <i>SMTP server</i>. All of this information is stored in a config file in the SMTP section.</p>

https://github.com/AleksaMCode/university-notices-email-notifier/blob/acc714b4f22fd296cc3f366e386770c5afec71f3/config.ini#L1-L6

### Yahoo SMTP
<p align="justify">Below you have a table of all the essential details you need:</p>

SMTP server | Port | Requires SSL | Requires TLS | Authentication | Username | Password |
-- | :--: | :--: | :--: | :--: | -- | -- |
smtp.mail.yahoo.com | 587 | ✅ | ✅ | ✅| Your Yahoo email address | Your Yahoo Mail App Password, which isn't the same as your account password |

> **Restrictions**:
> <ul><li>You can send maximum of 500 emails per day.</li>
> <li>Some sources claim you can send maximum of 100 emails per hour.</li></ul>

<p align="justify">In order to use Yahoo SMTP server, you need to create a dedicated App Password. Firstly you need to go to your account settings area and then click on <b>Account Security</b> after which you will click on <b>Generate app password</b> link under the <b>Other ways to sign in</b> section. After the popup is shown you will need to enter your app name, which can be anything. Next, click the <b>Generate password</b> button. You should then see the 16-char long app password, which you will need to remember for later usage as Yahoo will not be showing it to you again.</p>

## Scheduling scraping
### Windows - Task Scheduler
<p align="justify">First thing you need to create is a <i>bat</i> file which will connect the <i>python.exe</i> and <i>notifier.py</i> script. Open a directory in which you wish to create a <i>bat</i> file and open a powershell and type the following commands:</p>

```powershell
New-Item scraper.bat
"@echo of `r`n""C:\Users\Username\AppData\Local\Programs\Python\Python310\python.exe"" ""C:\Users\Username\university-notices-email-notifier\notifier.py"""
```

> **Note**:
> <br>You will need to adjust the syntax above:
> <ul><li>Set first path where your <i>python.exe</i> is stored.</li>
> <li>Set second path where <i>notifier.py</i> script is stored.</li></ul>

<p align="justify">In order to schedule the scraper using Window Scheduler you will need to:
<ul>
<li>Open the Windows Control Panel, then click on the <b>Administrative Tools</b> and double-click on the <b>Task Scheduler</b>.</li>
<li>Choose the option `<i>Create Task...</i>`.</li>
<li>Type a name for this task (description is optional) in <b>General</b> tab and then click on <b>Triggers</b> tab.</li>
<li>Press on the <b>New...</b> and then in the newly opened <i>New Trigger</i> window choose to start the task 'One time' starting from 12:00:00 am.</li>
<li>In <i>Advanced settings</i> tick 'Repeat task every' and enter your desired frequency.</li>
<li>From the drop menu <i>for a duration of</i> choose 'Indefinitely' and press on <b>OK</b>.
<li>Press on the <Actions> tab and click on the <b>New...</b> button. There you will need to browse and find <i>scraper.bat</i> which is located inside of the resources/scripts directory.</li>
<li>Press <b>OK</b> twice.</li>
</ul></p>

### Linux - Cron job
<p align="justify">Firstly you need to open crontab with the following command <code> crontab -e</code>. Once you enter the cron editor you will need to add the cronjob command. For example, if you want to run this scraper every 30 minutes you will enter:</p>

```shell
0,30 * * * * /usr/bin/python /home/script/university-notices-email-notifier/notifier.py
```

<p align="justify">Save your changes and exit the editor. For more details on how to specify frequency visit this <a href="https://www.adminschoice.com/crontab-quick-reference">link</a>.</p>

> **Note**:
> <br>Don't forget to exit Vim using <code>:wq</code>. :)

## To-Do List
- [ ] Replace json file attachment with html formated email response.
- [ ] Implement year specific command for notifications.
- [ ] Implement year range command for notifications.
- [ ] Move sensitive information, like password,  from config file to environment variables.
- [ ] Implement toast notifications.