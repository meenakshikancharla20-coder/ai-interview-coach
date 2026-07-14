# AI Interview Coach

A console-based mock interview tool built in Python that helps users practice 
common interview questions and receive instant, structured feedback to improve 
their responses.

## What it does
- Presents 3 randomly selected interview questions from a bank of common questions 
  (behavioral, HR, and technical-style)
- Evaluates each answer based on:
  - **Length** — checks if the response is too short, too long, or well-balanced
  - **Relevance** — scans for topic-relevant keywords related to the question
  - **Filler words** — flags words like "um," "like," "you know" that reduce 
    confidence in real interviews
- Scores each answer out of 10 based on these factors
- Tracks progress across multiple practice sessions using JSON-based history 
  storage, and shows whether the user is improving over time

## Key Feature
Unlike a simple Q&A tool, this project maintains persistent session history, 
allowing users to track their interview performance and improvement trend over 
multiple practice attempts.

## Tech Stack
- Python
- JSON (for progress tracking)

## Files
- `ai_interview_coach.py` - main program with question bank, scoring logic, and 
  session tracking
- `interview_history.json` - stores past practice session scores and answers

## How to run
1. Make sure Python is installed
2. Run `ai_interview_coach.py`
3. Choose "Start Mock Interview" and answer each question naturally
4. Review your feedback and score after each question
5. Run multiple sessions to track improvement over time

## Sample Output
