#!/usr/bin/env python
import sys
from dotenv import load_dotenv
load_dotenv()

from crew import ITSMBlogCrewTemplate

def run():
    """
    Run the crew.
    """
    inputs = {
        "blog_topic": "Latest Trends in ITSM Automation",
        "target_audience": "IT service professionals and managers",
        "key_focus_areas": "AI integration, process automation, and service optimization"
    }

    ITSMBlogCrewTemplate().crew().kickoff(inputs=inputs)

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "blog_topic": "ITSM Best Practices",
        "target_audience": "IT service professionals"
    }
    try:
        ITSMBlogCrewTemplate().crew().train(
            n_iterations=int(sys.argv[1]), 
            filename=sys.argv[2], 
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ITSMBlogCrewTemplate().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "blog_topic": "ITSM Automation Testing",
        "target_audience": "IT service professionals"
    }
    try:
        ITSMBlogCrewTemplate().crew().test(
            n_iterations=int(sys.argv[1]),
            openai_model_name=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    run()