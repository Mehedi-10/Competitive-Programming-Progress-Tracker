# Competitive Programming Progress Tracker

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Version](https://img.shields.io/badge/version-1.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Welcome to Competitive Programming Progress Tracker! This Django-based web application enables competitive programmers to effortlessly track their daily performance, receive personalized feedback, and stay on top of their progress.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

Competitive Programming Progress Tracker leverages Django's power to provide a robust platform for competitive programmers. By integrating APIs and utilizing web scraping techniques, the project gathers data from various online programming judges and websites. The result is an intuitive interface that empowers programmers to visualize their progress over time.

## Installation

To set up Competitive Programming Progress Tracker locally, follow these steps:

1. Clone the repository: `git clone https://github.com/Mehedi-10/Competitive-Programming-Progress-Tracker.git`
2. Navigate to the project directory: `cd Competitive-Programming-Progress-Tracker`
3. Create a virtual environment: `python3 -m venv venv`
4. Activate the virtual environment:
   - On macOS and Linux: `source venv/bin/activate`
   - On Windows: `venv\Scripts\activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Apply migrations: `python manage.py migrate`
7. Create a superuser account: `python manage.py createsuperuser`
8. Start the development server: `python manage.py runserver`

## Usage

After starting the development server, open your web browser and go to `http://localhost:8000`. You can create an account, log in, and begin tracking your daily programming activities. The user-friendly interface lets you visualize your progress over time and receive personalized feedback from experienced coaches.

## Features

- Seamlessly track your daily programming performance
- Gain insights into your progress through visualizations
- Receive personalized feedback from knowledgeable coaches
- User-friendly interface built using Django
- Integration with APIs of popular programming judges

## Contributing

Contributions to Competitive Programming Progress Tracker are welcomed! To contribute:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a pull request

For significant changes, please open an issue first to discuss the proposed changes.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

Have questions or suggestions? Feel free to contact me at `mehedihasanarafat@stud.cou.ac.bd`.
