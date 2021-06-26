# yorku-form-filler
YorkU Daily Covid Form filler

Installation process for Windows:
1) Install Chromedriver from here https://chromedriver.chromium.org/downloads 
2) Install Python from here https://www.python.org/downloads/ or full Anaconda package from here https://www.anaconda.com/products/individual
3) Using cmd or Anaconda prompt, install selenium python package with command "pip install selenium"
4) Download and open the fill_data.txt file and fill in your information. After "webdriver:" write the path to chromedriver.exe file. Save it.
5) Download the "Form filler public.py" file. Save it to the same folder as your fill_data.txt file.
6) Create a bat file that will run every day. To do so: 
6.1) Open Notepad program
6.2) Type in the path to your python.exe file, for example "C:\ProgramData\Anaconda3\python.exe" (no quotation marks) 
6.3) Add a space bar after 6.3 and type the path to the "Form filler public.py" file (with quotation marks)
6.4) Type in "pause" on the next line (no quotation marks) 
6.5) Save file as "all files" and add ".bat" extention at the end. 
7) Press Start Key / Win Button and type in "Task Scheduler"
7.1) In Actions click on "Create basic task", add some name and description, next
7.2) Choose daily frequency, recur every 1 day, choose a time when your PC is most likely to be on, next
7.3) Choose Start a program, next
7.4) Click browse and look for your .bat file, leave other fields blank and as is, click Finish

That's it
