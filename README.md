#  PR. 1: Fundamental Booster (Interactive Personal Data Collector)

A Python-based interactive command-line application that acts as a **Personal Data Collector**. This project demonstrates the practical application of fundamental programming principles including data type identification, explicit type casting, dynamic memory tracking, and basic mathematical operations.

---

## 🛠️ Tech Stack & Key Concepts Demonstrated
* **Language:** Python 3
* **Data Input/Output:** Leveraging `input()` and formatted f-strings for seamless CLI interaction.
* **Type Conversion (Casting):** Explicitly converting string inputs into operational `int` and `float` data types.
* **Memory Management Insights:** Utilizing built-in `type()` and `id()` functions to inspect data types and their dynamic memory addresses in real-time.
* **Data Processing:** Performing algorithmic calculation to derive the approximate birth year based on the current year (2026) and user input.

---

##  How It Works (Execution Output Example)

When executed, the script prompts the user for information, maps the variables in memory, and displays the processed dashboard:

```text
Welcome to the Interactive Personal Data Collector!

Please enter your name: Shaikh
Please enter your age: 18
Please enter your height in meters: 5.6
Please enter your favourite number: 1

Thank you! Here is the information we collected:

Name: shaikh (Type: <class 'str'>, Memory Address: 2686730393984)
Age: 18 (Type: <class 'int'>, Memory Address: 140709188126360)
Height: 5.6 (Type: <class 'float'>, Memory Address: 2686727336848)
Favourite Number: 1 (Type: <class 'int'>, Memory Address: 140709188125816)

Your birth year is approximately: 2008 (based on your age of 18)

Thank you for using the Personal Data Collector. Goodbye!
