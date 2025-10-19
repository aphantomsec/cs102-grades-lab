#!/usr/bin/env python3
"""
CS102 Lab — Grades manager
Usage: python lab.py students.csv
CSV format: name,assignment1,assignment2,midterm,final
Example row: Alice,85,92,78,90
"""

import csv
import sys
from statistics import mean

def load_grades(path):
    students = []
    try:
        with open(path, newline='') as f:
            for row in csv.reader(f):
                if not row: 
                    continue
                name = row[0].strip()
                scores = [float(x) for x in row[1:] if x.strip() != ""]
                students.append({"name": name, "scores": scores})
    except FileNotFoundError:
        print(f"Error: file not found: {path}")
        sys.exit(1)
    return students

def compute_final(score_list, weights=(0.2,0.2,0.25,0.35)):
    # Accept variable-length but assume first 4 map to weights
    scores = list(score_list) + [0]*4
    return sum(s * w for s, w in zip(scores[:4], weights))

def summarize(students):
    for s in students:
        s["final"] = round(compute_final(s["scores"]), 2)
    finals = [s["final"] for s in students] or [0]
    return {
        "count": len(students),
        "min": min(finals),
        "max": max(finals),
        "avg": round(mean(finals), 2)
    }

def top_n(students, n=3):
    return sorted(students, key=lambda s: s["final"], reverse=True)[:n]

def save_report(path, students, summary):
    with open(path, "w", newline='') as f:
        w = csv.writer(f)
        w.writerow(["name","final"])
        for s in students:
            w.writerow([s["name"], s["final"]])
        w.writerow([])
        w.writerow(["count","min","max","avg"])
        w.writerow([summary["count"], summary["min"], summary["max"], summary["avg"]])

def main(csv_path):
    students = load_grades(csv_path)
    if not students:
        print("No student data found.")
        return
    summary = summarize(students)
    print(f"Students: {summary['count']}  Avg: {summary['avg']}  Min: {summary['min']}  Max: {summary['max']}")
    print("\nTop 3 students:")
    for s in top_n(students, 3):
        print(f"  {s['name']:15} {s['final']}")
    out = csv_path.rsplit(".",1)[0] + "_report.csv"
    save_report(out, students, summary)
    print(f"\nReport saved to {out}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python lab.py students.csv")
        sys.exit(1)
    main(sys.argv[1])
