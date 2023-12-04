# :rocket: CourseRekt
## [Visit the website here!](https://courserekt.vercel.app/) :computer:

![Image of the website](docs/images/preview.png)

## Purpose

It is rather unfortunate that NUS does not keep a record of the Demand Allocation Reports. Furthermore, the data is presented in such a verbose and hard-to-visualise way. This app aims to streamline this process, making analysis of a course's past popularity more accessible and straightforward.

## For Users:

### Search Bar

You can delimit your search with spaces. For example, "AC5001 CS2" will show all course codes that have "AC5001" or "CS2" in its name.

### Accessing the PDF data

You can click the column headers to access the raw PDF data used to generate the table for the respective year, semester, and undergraduate/graduate type.

### Interpreting table cells

Each cell corresponds to the data in the PDF for the course's class and round number, in the format `x / y`, where `x` is the `Demand` and y is the `Vacancy` as per the PDF.

- If `y` is displayed as `∞`, the `Vacancy` in the PDF is `-`.
- If `N/A` is displayed, then the class data was not found in this PDF.

## Contributing

Please refer to `CONTRIBUTING.md` for more information.

Feel free to fork the project, make some changes, and submit a pull request. If you find any bugs or have any suggestions, please open an issue. All contributions are welcomed!

## Contributors

Thank you to all of our contributors!

<a href="https://github.com/et-irl/courserekt/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=et-irl/courserekt" />
</a>

Made with [contrib.rocks](https://contrib.rocks).
