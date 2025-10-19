#!/usr/bin/env python3
"""
Unit tests for CS102 Grades Lab
"""

import unittest
import os
import tempfile
from grades import GradeAnalyzer


class TestGradeAnalyzer(unittest.TestCase):
    """Test cases for GradeAnalyzer class."""
    
    def setUp(self):
        """Set up test fixtures."""
        # Create a temporary CSV file for testing
        self.test_csv = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv')
        self.test_csv.write("Name,Homework,Midterm,Final\n")
        self.test_csv.write("Student A,80,85,90\n")
        self.test_csv.write("Student B,90,90,90\n")
        self.test_csv.write("Student C,70,75,80\n")
        self.test_csv.close()
        
        self.analyzer = GradeAnalyzer(self.test_csv.name)
        self.analyzer.read_grades()
    
    def tearDown(self):
        """Clean up test fixtures."""
        os.unlink(self.test_csv.name)
    
    def test_read_grades(self):
        """Test reading grades from CSV file."""
        self.assertEqual(len(self.analyzer.students), 3)
        self.assertEqual(self.analyzer.students[0]['name'], 'Student A')
    
    def test_calculate_final_grade(self):
        """Test weighted grade calculation."""
        student = {
            'homework': 80,
            'midterm': 85,
            'final': 90
        }
        grade = self.analyzer.calculate_final_grade(student)
        # 80*0.3 + 85*0.3 + 90*0.4 = 24 + 25.5 + 36 = 85.5
        self.assertEqual(grade, 85.5)
    
    def test_get_letter_grade(self):
        """Test letter grade conversion."""
        self.assertEqual(self.analyzer.get_letter_grade(95), 'A')
        self.assertEqual(self.analyzer.get_letter_grade(85), 'B')
        self.assertEqual(self.analyzer.get_letter_grade(75), 'C')
        self.assertEqual(self.analyzer.get_letter_grade(65), 'D')
        self.assertEqual(self.analyzer.get_letter_grade(55), 'F')
    
    def test_get_statistics(self):
        """Test statistics calculation."""
        stats = self.analyzer.get_statistics()
        self.assertIsNotNone(stats)
        self.assertIn('average', stats)
        self.assertIn('min', stats)
        self.assertIn('max', stats)
        self.assertIn('std_dev', stats)
        # Student A: 80*0.3 + 85*0.3 + 90*0.4 = 85.5
        # Student B: 90*0.3 + 90*0.3 + 90*0.4 = 90.0
        # Student C: 70*0.3 + 75*0.3 + 80*0.4 = 75.5
        self.assertEqual(stats['max'], 90.0)
        self.assertEqual(stats['min'], 75.5)
    
    def test_get_top_performers(self):
        """Test top performers identification."""
        top = self.analyzer.get_top_performers(2)
        self.assertEqual(len(top), 2)
        self.assertEqual(top[0]['name'], 'Student B')
        self.assertEqual(top[0]['grade'], 90.0)
    
    def test_file_not_found(self):
        """Test handling of non-existent file."""
        analyzer = GradeAnalyzer('nonexistent.csv')
        result = analyzer.read_grades()
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
