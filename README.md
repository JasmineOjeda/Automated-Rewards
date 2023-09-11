# **Automated Rewards**
Automates the procedures to gain daily rewards from MS rewards program! It is specifically designed for Windows users whose default browser is MS Edge. The procedures and activities it will perform:
- Desktop and mobile searches with randomly generated strings
- Click on daily sets and activities
- Click and complete the monthly punch-card
- Complete quizzes and polls (randomly or accurately depending on optimization of points)

Written in Python 3.10.4 with Selenium.

To install Selenium: ```pip install selenium```

To install Beautiful Soup: ```pip install bs4```

To run the program: ```python main.py```



## Other Notes
It is ***highly*** recommended to create a copy of your system's Edge User Data directory (name it "Temp User Data") to use as to avoid unintentional changes to your own browser and profile.

Create an ```info.json``` file in the following format, replacing all text in between <> accordingly:
```
{
    "username": "<Your MS email>",
    "password": "<Your MS password>",
    "userDataDir": "<The path to your MS Edge 'Temp User Data' director>",
    "binaryLocation": "<The path to yoursystem's msedge.exe>"
}
```
Feel free to add, remove, and edit entries to the existing txt files in the ```dictionary``` folder to generate more personalized random searches. Make sure to always separate entries by commas and that all entries are on the same line!