#!/usr/bin/env python3
"""
CS102 Grades Lab - Student Grade Management and Analysis
This script reads student grades from a CSV file, calculates final grades
using weighted averages, and outputs a summary report with statistics.
"""

import csv
import sys
from statistics import mean, stdev


class GradeAnalyzer:
    """Analyzes student grades and generates reports."""
    
    # Weighted grade calculation: Homework 30%, Midterm 30%, Final 40%
    WEIGHTS = {
        'Homework': 0.30,
        'Midterm': 0.30,
        'Final': 0.40
    }
    
    def __init__(self, csv_file):
        """Initialize the GradeAnalyzer with a CSV file."""
        self.csv_file = csv_file
        self.students = []
        
    def read_grades(self):
        """Read student grades from CSV file."""
        try:
            with open(self.csv_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = {
                        'name': row['Name'],
                        'homework': float(row['Homework']),
                        'midterm': float(row['Midterm']),
                        'final': float(row['Final'])
                    }
                    student['grade'] = self.calculate_final_grade(student)
                    student['letter'] = self.get_letter_grade(student['grade'])
                    self.students.append(student)
            return True
        except FileNotFoundError:
            print(f"Error: File '{self.csv_file}' not found.")
            return False
        except Exception as e:
            print(f"Error reading file: {e}")
            return False
    
    def calculate_final_grade(self, student):
        """Calculate weighted final grade for a student."""
        grade = (
            student['homework'] * self.WEIGHTS['Homework'] +
            student['midterm'] * self.WEIGHTS['Midterm'] +
            student['final'] * self.WEIGHTS['Final']
        )
        return round(grade, 2)
    
    def get_letter_grade(self, grade):
        """Convert numerical grade to letter grade."""
        if grade >= 90:
            return 'A'
        elif grade >= 80:
            return 'B'
        elif grade >= 70:
            return 'C'
        elif grade >= 60:
            return 'D'
        else:
            return 'F'
    
    def get_statistics(self):
        """Calculate statistics for all final grades."""
        if not self.students:
            return None
        
        final_grades = [s['grade'] for s in self.students]
        stats = {
            'average': round(mean(final_grades), 2),
            'min': min(final_grades),
            'max': max(final_grades),
            'std_dev': round(stdev(final_grades), 2) if len(final_grades) > 1 else 0
        }
        return stats
    
    def get_top_performers(self, n=3):
        """Get top n performers by final grade."""
        sorted_students = sorted(self.students, key=lambda x: x['grade'], reverse=True)
        return sorted_students[:n]
    
    def print_report(self):
        """Print comprehensive grade report."""
        if not self.students:
            print("No student data available.")
            return
        
        print("=" * 70)
        print("CS102 GRADE REPORT")
        print("=" * 70)
        print()
        
        # Individual student grades
        print("INDIVIDUAL GRADES")
        print("-" * 70)
        print(f"{'Name':<20} {'HW':>6} {'Mid':>6} {'Final':>6} {'Grade':>6} {'Letter':>6}")
        print("-" * 70)
        for student in self.students:
            print(f"{student['name']:<20} {student['homework']:>6.0f} "
                  f"{student['midterm']:>6.0f} {student['final']:>6.0f} "
                  f"{student['grade']:>6.2f} {student['letter']:>6}")
        print()
        
        # Statistics
        stats = self.get_statistics()
        print("STATISTICS")
        print("-" * 70)
        print(f"Average Grade:        {stats['average']:.2f}")
        print(f"Minimum Grade:        {stats['min']:.2f}")
        print(f"Maximum Grade:        {stats['max']:.2f}")
        print(f"Standard Deviation:   {stats['std_dev']:.2f}")
        print()
        
        # Top performers
        top_performers = self.get_top_performers()
        print("TOP PERFORMERS")
        print("-" * 70)
        for i, student in enumerate(top_performers, 1):
            print(f"{i}. {student['name']:<20} - {student['grade']:.2f} ({student['letter']})")
        print()
        print("=" * 70)


def main():
    """Main function to run the grade analyzer."""
    # Default CSV file
    csv_file = 'students.csv'
    
    # Allow command-line argument for custom CSV file
    if len(sys.argv) > 1:
        csv_file = sys.argv[1]
    
    analyzer = GradeAnalyzer(csv_file)
    
    if analyzer.read_grades():
        analyzer.print_report()
    else:
        sys.exit(1)


if __name__ == '__main__':
    main()
