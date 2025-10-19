# CS102 Grades Lab

A simple Python script for managing and analyzing student grades in a CS102 course. This lab demonstrates file I/O, data processing, and statistical analysis using Python.

## Features

- **CSV File Reading**: Reads student names and scores from a CSV file
- **Weighted Average Calculation**: Calculates final grades using configurable weights:
  - Homework: 30%
  - Midterm: 30%
  - Final Exam: 40%
- **Letter Grades**: Converts numerical grades to letter grades (A-F)
- **Summary Statistics**: Calculates and displays:
  - Average grade
  - Minimum grade
  - Maximum grade
  - Standard deviation
- **Top Performers**: Identifies and displays the top 3 students

## Files

- `grades.py` - Main script for grade analysis
- `students.csv` - Sample student data file
- `test_grades.py` - Unit tests for the grade analyzer

## Usage

### Basic Usage

Run the script with the default `students.csv` file:

```bash
python3 grades.py
```

### Custom CSV File

Specify a custom CSV file:

```bash
python3 grades.py path/to/your/grades.csv
```

### CSV File Format

The CSV file should have the following format:

```csv
Name,Homework,Midterm,Final
Alice Johnson,85,78,92
Bob Smith,92,88,85
```

Required columns:
- `Name` - Student name
- `Homework` - Homework score (0-100)
- `Midterm` - Midterm exam score (0-100)
- `Final` - Final exam score (0-100)

## Example Output

```
======================================================================
CS102 GRADE REPORT
======================================================================

INDIVIDUAL GRADES
----------------------------------------------------------------------
Name                     HW    Mid  Final  Grade Letter
----------------------------------------------------------------------
Alice Johnson            85     78     92  85.70      B
Bob Smith                92     88     85  88.00      B
Diana Wilson             95     92     96  94.50      A

STATISTICS
----------------------------------------------------------------------
Average Grade:        86.45
Minimum Grade:        76.10
Maximum Grade:        94.50
Standard Deviation:   5.84

TOP PERFORMERS
----------------------------------------------------------------------
1. Diana Wilson         - 94.50 (A)
2. Grace Lee            - 92.70 (A)
3. Ivy Anderson         - 92.20 (A)

======================================================================
```

## Running Tests

Execute the unit tests to verify functionality:

```bash
python3 -m unittest test_grades.py -v
```

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Grading Scale

- A: 90-100
- B: 80-89
- C: 70-79
- D: 60-69
- F: Below 60

## License

This is a simple educational lab project for CS102.