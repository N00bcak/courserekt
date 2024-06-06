import argparse
import subprocess


def build(
    year: str = "*",
    semester: str = "*",
    student_type: str = "*",
    round_no: str = "*",
) -> None:
    round_no = f"round_{round_no}" if round_no == "*" else round_no

    # Define script paths
    convert_pdfs_script = "src/history/convert_pdfs.py"
    clean_vh_csvs_script = "src/history/vacancy_history/clean_csvs.py"
    clean_crh_csvs_script = "src/history/coursereg_history/clean_csvs.py"
    import_csv_to_db_script = "src/history/import_csv_to_db.py"
    merge_db_script = "src/history/merge_db.py"

    # Define input directories
    vh_pdfs_glob = f"src/history/vacancy_history/data/pdfs/{year}/{semester}/{round_no}.pdf"  # noqa: E501
    crh_pdfs_glob = f"src/history/coursereg_history/data/pdfs/{year}/{semester}/{student_type}/{round_no}.pdf"  # noqa: E501
    vh_raw_csvs_glob = "src/history/vacancy_history/data/raw/*/*/*.csv"
    crh_raw_csvs_glob = "src/history/coursereg_history/data/raw/*/*/*/*.csv"
    vh_cleaned_csvs_glob = "src/history/vacancy_history/data/cleaned/*/*/*.csv"
    crh_cleaned_csvs_glob = "src/history/coursereg_history/data/cleaned/*/*/*/*.csv"

    print("Converting PDFs to CSVs...")
    print("Please be patient. This might take some time.")
    subprocess.run(f"time python {convert_pdfs_script} {vh_pdfs_glob} {crh_pdfs_glob}",
                   shell=True, check=True)

    print("Cleaning Vacancy CSVs...")
    subprocess.run(f"python {clean_vh_csvs_script} -i {vh_raw_csvs_glob}",
                   shell=True, check=True)

    print("Cleaning CourseReg CSVs...")
    subprocess.run(f"python {clean_crh_csvs_script} -i {crh_raw_csvs_glob}",
                   shell=True, check=True)

    print("Importing CSV files to database...")
    subprocess.run(f"python {import_csv_to_db_script} {vh_cleaned_csvs_glob} {crh_cleaned_csvs_glob}",  # noqa: E501
                   shell=True, check=True)

    print("Merging Vacancy and CourseReg data...")
    subprocess.run(f"python {merge_db_script} {crh_cleaned_csvs_glob}",
                   shell=True, check=True)

    print("Database created!")


# Define accepted values for year and semester
YEAR_CHOICES = ("2122", "2223", "2324")
SEMESTER_CHOICES = ("1", "2")
TYPE_CHOICES = ("ug", "gd")
ROUND_CHOICES = ("0", "1", "2", "3")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the database")

    # Add optional year argument
    parser.add_argument(
        "--year", "-y",
        choices=YEAR_CHOICES,
        help="Year to process (e.g., 2223)",
        default="*",
    )

    # Add optional semester argument
    parser.add_argument(
        "--semester", "-s",
        choices=SEMESTER_CHOICES,
        help="Semester to process (1 or 2)",
        default="*",
    )

    # Add optional type argument
    parser.add_argument(
        "--student-type", "-t",
        choices=TYPE_CHOICES,
        help="Type of courses to process (ug or gd)",
        default="*",
    )

    # Add optional round argument
    parser.add_argument(
        "--round", "-r",
        choices=ROUND_CHOICES,
        help="Round to process (0 or 1 or 2 or 3)",
        default="*",
    )

    args = parser.parse_args()

    build(
        year=args.year,
        semester=args.semester,
        student_type=args.student_type,
        round_no=args.round,
    )


if __name__ == "__main__":
    main()
