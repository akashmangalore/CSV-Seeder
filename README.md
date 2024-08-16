<p align="center">
  <img src="logo.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">CSV-SEEDER</h1>
</p>
<p align="center">
    <em>Effortless Synthetic Data for Seamless CSV Workflows</em>
</p>
<p align="center">
 <img src="https://img.shields.io/github/license/akashmangalore/CSV-Seeder?style=flat&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
 <img src="https://img.shields.io/github/last-commit/akashmangalore/CSV-Seeder?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
 <img src="https://img.shields.io/github/languages/top/akashmangalore/CSV-Seeder?style=flat&color=0080ff" alt="repo-top-language">
 <img src="https://img.shields.io/github/languages/count/akashmangalore/CSV-Seeder?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
  <em>Developed with the software and tools below.</em>
</p>
<p align="center">
 <img src="https://img.shields.io/badge/Python-Language-3776AB.svg?style=flat&logo=Python" alt="Python">
   <img alt="Mimesis" src="https://img.shields.io/badge/Mimesis-Fake%20Data%20Generator-45FFCA?style=flat&link=https%3A%2F%2Fmimesis.name">
 <img src="https://img.shields.io/badge/Pandas-Data%20Analysis%20Tool-150458.svg?style=flat&logo=pandas" alt="Pandas">
   <img src="https://img.shields.io/badge/Gradio-UI%20Framework-FF8C2E?style=flat&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjQwIiBoZWlnaHQ9IjQ4MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZGVmcz48bGluZWFyR3JhZGllbnQgaWQ9ImEiIHgxPSItLjA2IiB4Mj0iLjg1IiB5MT0iLjUiIHkyPSIuNSI+PHN0b3Agc3RvcC1jb2xvcj0iI0Y5RDEwMCIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iI0Y5NzcwMCIvPjwvbGluZWFyR3JhZGllbnQ+PGxpbmVhckdyYWRpZW50IGlkPSJiIiB4MT0iMS4wNiIgeDI9Ii4xNCIgeTE9Ii41IiB5Mj0iLjUiPjxzdG9wIHN0b3AtY29sb3I9IiNGOUQxMDAiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiNGOTc3MDAiLz48L2xpbmVhckdyYWRpZW50PjxsaW5lYXJHcmFkaWVudCBpZD0iYyIgeDE9Ii0uMTMiIHgyPSIxLjciIHkxPSIxIiB5Mj0iLjk4Ij48c3RvcCBzdG9wLWNvbG9yPSIjRjlEMTAwIi8+PHN0b3Agb2Zmc2V0PSIxIiBzdG9wLWNvbG9yPSIjRjk3NzAwIi8+PC9saW5lYXJHcmFkaWVudD48L2RlZnM+PGcgY2xhc3M9ImxheWVyIiBzdHJva2Utd2lkdGg9IjU5Ij48cGF0aCBkPSJNMzA3LjUgMTgxIDEwNiAyOTYuNSAzMDcuNSA0MTIgNTA5IDI5Ni41eiIgc3Ryb2tlPSJ1cmwoI2EpIiBzdHJva2UtbGluZWpvaW49InJvdW5kIi8+PHBhdGggZD0iTTMwNy41IDY4IDEwNiAxODMuNSAzMDcuNSAyOTkgNTA5IDE4My41eiIgc3Ryb2tlPSJ1cmwoI2IpIiBzdHJva2UtbGluZWpvaW49InJvdW5kIi8+PHBhdGggZD0ibTEwNiAyOTYgMjAyLTExNSIgc3Ryb2tlPSJ1cmwoI2MpIiBzdHJva2UtbGluZWpvaW49ImJldmVsIi8+PC9nPjwvc3ZnPg==&logoColor=white" alt="Gradio">
   <img src="https://img.shields.io/badge/Poetry-Package%20Management-60A5FA.svg?style=flat&logo=Poetry" alt="Poetry">
</p>

<details>
  <summary>Table of Contents</summary><br>

- [📍 Overview](#-overview)
- [🧩 Features](#-features)
- [🗂️ Repository Structure](#️-repository-structure)
- [📦 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [⚙️ Installation](#️-installation)
  - [🤖 Usage](#-usage)
  - [🧪 Tests](#-tests)
- [🤝 Contributing](#-contributing)
- [🎗 License](#-license)
- [🔗 Acknowledgments](#-acknowledgments)

</details>
<hr>

## 📍 Overview

CSV-Seeder is an efficient software tool designed to generate synthetic CSV data tailored to user-defined specifications. It leverages Mimesis for data generation and Pandas for seamless CSV manipulation. The project boasts a user-friendly Gradio interface for uploading templates, customizing data generation methods, and producing downloadable records. Managed via the pyproject.toml file, CSV-Seeder ensures smooth configuration, dependency handling, and project maintenance. This tool is invaluable for developers and testers needing realistic synthetic datasets for testing, development, and data analysis workflows.

---

## 🧩 Features

|      | Feature                 | Description                                                                                                                                                                   |
| ---- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ⚙️ | **Architecture**  | The project follows a modular architecture with a clear separation between configuration, main functionality, and user interface components.                                  |
| 🔩   | **Code Quality**  | The code quality is decent but could benefit from more consistent styling and additional comments to improve readability and maintainability.                                 |
| 📄   | **Documentation** | Basic documentation is present through `pyproject.toml` and code comments, but it lacks comprehensive usage guides and examples.                                            |
| 🔌   | **Integrations**  | Integrates Gradio for the UI, Mimesis for data generation, and Pandas for CSV manipulation, making it a versatile tool for CSV data seeding.                                  |
| 🧩   | **Modularity**    | The main functionality is encapsulated in `csv_seeder/main.py`, suggesting good modularity. Functions are reusable but could be further broken down for better decoupling.  |
| 🧪   | **Testing**       | No explicit testing frameworks or test cases are mentioned or found in the repository, indicating a need for additional testing infrastructure.                               |
| ⚡️ | **Performance**   | The performance is largely dependent on the efficiency of Pandas and Mimesis. Suitable for small to medium-sized CSV files but not optimized for very large datasets.         |
| 🛡️ | **Security**      | No explicit security measures such as input validation or access control are mentioned; relies on the inherent security of the used libraries.                                |
| 📦   | **Dependencies**  | Utilizes key external libraries like `gradio`, `pandas`, `mimesis`, `pydash`, `pytz`, and `toml`, which are essential for its functionality.                      |
| 🚀   | **Scalability**   | Designed to handle typical CSV data generation tasks, but scalability might be limited due to potential performance bottlenecks with very large datasets or high concurrency. |

---

## 🗂️ Repository Structure

```sh
└── CSV-Seeder/
    ├── LICENSE
    ├── README.md
    ├── csv_seeder
    │   ├── __init__.py
    │   └── main.py
    ├── poetry.lock
    ├── pyproject.toml
    └── tests
        └── __init__.py
```

---

## 📦 Modules

<details closed><summary>.</summary>

| File                                                                                   | Summary                                                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [pyproject.toml](https://github.com/akashmangalore/CSV-Seeder/blob/master/pyproject.toml) | Orchestrates project configuration, including metadata, dependencies, build system settings, and linting rules, essential for managing and maintaining the CSV-Seeder project effectively within the repositorys architecture. |

</details>

<details closed><summary>csv_seeder</summary>

| File                                                                                | Summary                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [main.py](https://github.com/akashmangalore/CSV-Seeder/blob/master/csv_seeder/main.py) | Main functionality focuses on generating synthetic CSV data based on user-defined headers, methods, and locales. Includes a Gradio interface for uploading CSV files, selecting data generation methods, and generating downloadable CSV records. Integrates Mimesis for data generation and Pandas for CSV manipulation, enhancing data seeding capabilities. |

</details>

---

## 🚀 Getting Started

**System Requirements:**

- **Python**: `version 3.12`

### ⚙️ Installation

<h4>From <code>source</code></h4>

> 1. Clone the CSV-Seeder repository:
>
> ```console
> $ git clone https://github.com/akashmangalore/CSV-Seeder
> ```
>
> 2. Change to the project directory:
>
> ```console
> $ cd CSV-Seeder
> ```
>
> 3. Install the dependencies:
>
> ```console
> $ pip install -r requirements.txt
> ```

### 🤖 Usage

<h4>From <code>source</code></h4>

> Run CSV-Seeder using the command below:
>
> ```console
> $ python main.py
> # Or
> $ gradio main.py
> ```

### 🧪 Tests

> Run the test suite using the command below:
>
> ```console
> $ pytest
> ```

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/akashmangalore/CSV-Seeder/issues)**: Submit bugs found or log feature requests for the `CSV-Seeder` project.
- **[Submit Pull Requests](https://github.com/akashmangalore/CSV-Seeder/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/akashmangalore/CSV-Seeder/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.

   ```sh
   git clone https://github.com/akashmangalore/CSV-Seeder.git
   ```

3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.

   ```sh
   git checkout -b new-feature-x
   ```

4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.

   ```sh
   git commit -m 'Implemented new feature x.'
   ```

6. **Push to github**: Push the changes to your forked repository.

   ```sh
   git push origin new-feature-x
   ```

7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!

</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://github.com{/akashmangalore/CSV-Seeder/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=akashmangalore/CSV-Seeder">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the [MIT License](LICENSE) License. For more details, refer to the [LICENSE](LICENSE) file.

---

## 🔗 Acknowledgments

[**Return**](#-overview)

---
