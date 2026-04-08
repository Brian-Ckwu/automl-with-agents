"""
Evaluation script for scoring model predictions against ground-truth labels.

Usage: uv run evaluate.py --predictions_csv <path> --labels_csv <path>

This script takes two CSV files — one with model predictions and one with ground-truth
labels — and prints a single float to stdout representing the score. This file is read-only and should not be edited by the agent.

Implement the evaluation metric appropriate for your task below.
"""