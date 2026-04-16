# Python Learning Journey: 10 Practical Projects 🚀

This repository contains a collection of Python projects developed as part of the **"Learn Python By Coding: 10 Projects"** course by Federico Azzurro (Idently). Each project focuses on solving real-world problems while implementing core programming concepts and industry best practices.

---

## 📈 1. Personal Finance Calculator
A comprehensive tool designed to help users manage their personal economy by calculating taxes, net income, and savings.

* **Key Features:**
    * Dynamic calculation of monthly and yearly taxes based on user-provided rates.
    * Detailed breakdown of net income and potential annual savings.
    * Debt alert system if expenses exceed income.
* **Technical Highlights:**
    * Implementation of **input validation** loops to handle `ValueError`.
    * Advanced **string formatting** for currency display (commas for thousands and two-decimal precision).
    * Modular code structure with a clear separation of logic and user interaction.

---

## 💸 2. Expense Splitter
A utility to simplify group expenses, allowing users to split bills either equally or by specific percentages.

* **Key Features:**
    * **Equal Split:** Automatically divides the total amount by the number of participants.
    * **Uneven Split:** Allows users to assign custom percentages to each person.
    * **Percentage Guard:** Includes a logic check to ensure the total distribution does not exceed 100%, with a warning system for proportional adjustment.
* **Technical Highlights:**
    * Use of **Enumeration** (`enumerate`) to track participants during custom input.
    * Advanced logic for handling floating-point precision errors using `abs()` and small epsilon values.
    * Robust data gathering using custom helper functions for `int` and `float` types.

---

## 📊 3. Word Frequency Analyzer
A powerful text processing tool that reads multiple file formats to identify the most frequently used words while filtering out common "noise".

* **Key Features:**
    * **Multi-format Support:** Reads and processes `.txt`, `.pdf`, and `.docx` files.
    * **Stopword Filtering:** Includes a custom list of "noise" words (in both English and Spanish) to ensure results are meaningful.
    * **Cleaning Logic:** Removes punctuation and normalizes text to lowercase for accurate counting.
* **Technical Highlights:**
    * Extensive use of **Regular Expressions (Regex)** for sophisticated text tokenization.
    * Leverages the **`collections.Counter`** class for efficient frequency mapping.
    * Integration of external libraries such as `pypdf` for PDF parsing and `python-docx` for Word documents.
    * Implements **Error Handling** for file existence and unsupported formats.

---

## 📝 4. Simple Notepad (GUI)
A lightweight desktop application built to create, open, and save text files with a clean graphical user interface.

* **Key Features:**
    * **Full File Lifecycle:** Ability to create new files, open existing ones, and save changes locally.
    * **Dynamic Title Bar:** The window title updates automatically to show the name of the currently active file.
    * **Safety Checks:** Implements error dialogs to alert the user if a file fails to load or save.
* **Technical Highlights:**
    * Built using **Tkinter**, Python's standard GUI library.
    * Implements **Object-Oriented Programming (OOP)** to manage the application state and UI components.
    * Utilizes the `filedialog` and `messagebox` modules for professional OS-level interaction.
    * Uses `os.path` for intelligent filename parsing and path management.

---

## 🌐 5. Website Status Checker
A diagnostic tool that pings URLs to retrieve real-time data about server health and response metadata.

* **Key Features:**
    * **Connectivity Reports:** Displays HTTP status codes (e.g., 200 OK, 404 Not Found).
    * **Server Insights:** Extracts headers to identify server types (e.g., Nginx, Cloudflare) and content types.
    * **Performance Metrics:** Measures response time in seconds to evaluate website latency.
* **Technical Highlights:**
    * Extensive use of the **`requests`** library for handling HTTP protocols.
    * Implementation of **Exception Handling** (`RequestException`) to manage connection timeouts or invalid URLs.
    * Practical application of **Dictionaries** to parse complex HTTP header structures.

---

## 💱 6. Currency Converter (Local & API Logic)
A financial tool that performs currency conversions by calculating exchange rates between multiple global currencies.

* **Key Features:**
    * **Flexible Conversion:** Supports converting any currency pair (e.g., USD to CLP) using a base reference (EUR).
    * **Smart Validation:** Validates user input and provides a list of random "available options" if an invalid currency code is entered.
    * **Data Persistence:** Loads and parses exchange rates from external JSON data.
* **Technical Highlights:**
    * **JSON Integration:** Uses the `json` module to read and process structured database files.
    * **Dynamic Path Finding:** Implements a robust `get_file_path` function to ensure the script finds its data regardless of where it is executed in the system.
    * **Advanced Logic:** Handles relative rates through a pivot system (Base -> Reference -> Target).
    * **System Control:** Uses the `sys` and `os` modules for graceful program termination and directory navigation.

---

## 🔐 7. Secure Password Generator
A security tool that generates cryptographically strong passwords and evaluates their safety level.

* **Key Features:**
    * **Custom Complexity:** Users can toggle uppercase letters, digits, and special characters.
    * **Strength Evaluator:** A built-in logic that audits passwords based on length and character diversity.
    * **Batch Testing:** Main execution generates and audits 10 random variations to demonstrate range.
* **Technical Highlights:**
    * Uses the **`secrets`** module instead of `random` for true cryptographically secure tokens.
    * Implements a **Password Class** with advanced auditing methods using List Comprehensions and `any()`.
    * Leverages the `string` module for clean character set management.

---

## 🔍 8. Automated Text Analyzer
A statistics tool that provides a deep dive into the composition of any text file.

* **Key Features:**
    * **Metric Tracking:** Calculates total characters (with/without spaces), space frequency, and word count.
    * **Vocabulary Insight:** Identifies the top 5 most frequently used words, excluding punctuation.
    * **Human-Readable Reports:** Formats the output into a clean, aligned table for easy reading.
* **Technical Highlights:**
    * Professional file handling with absolute path resolution via `os.path`.
    * Use of `str.maketrans` for high-performance punctuation removal.
    * Data visualization logic using **f-string padding** (`:<35`) for perfect console alignment.

---

## 📟 9. Morse Code Translator & Communicator
A dual-purpose utility that translates text to Morse code and "broadcasts" it using system sound signals.

* **Key Features:**
    * **Bidirectional Logic:** Encodes plain text to Morse and decodes Morse signals back to text.
    * **Audio Transmission:** Uses the `winsound` library to play the actual "dots" and "dashes" through the PC speaker.
    * **Complete Character Map:** Supports letters, numbers, and common punctuation marks.
* **Technical Highlights:**
    * Implementation of **Dictionary Comprehension** to create a reverse lookup table efficiently.
    * Precise timing control with the `time` module to match Morse telegraphy standards.
    * Advanced string manipulation for joining and splitting encoded signals.

---

## 🤖 10. Intelligent ChatBot (Bob)
A sophisticated conversational agent that uses fuzzy logic for intent detection and integrates live external data.

* **Key Features:**
    * **Natural Language Processing:** Uses string similarity algorithms to understand user intent even with typos.
    * **Live Weather Integration:** Fetches real-time weather data for any city mentioned in the chat.
    * **Contextual Entity Extraction:** Uses Regular Expressions (Regex) to "pull" city names out of complex sentences.
* **Technical Highlights:**
    * **Asynchronous Programming:** Utilizes `asyncio` and `python_weather` for non-blocking API calls.
    * **Fuzzy Matching:** Implements `difflib.SequenceMatcher` to calculate similarity ratios.
    * **Advanced Regex:** Employs Case-Insensitive Non-Capturing Groups to parse user entities dynamically.
    * **Fallback Logic:** Includes a confidence threshold (50%) to handle unknown queries gracefully.

---

### 🎓 Final Notes
This project series represents a transition from basic scriptwriting to full-scale application development, covering **GUIs, APIs, Asynchronous logic, and Object-Oriented Programming.**

Feel free to explore the folders and run the code!
