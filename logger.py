from pybricks.tools import wait, StopWatch, multitask, run_task
from bob import Bob

# Global state for logging
logging_active = False
all_done = False

async def log_movements(bob: Bob):
    """Log robot movements continuously while logging is active"""
    global logging_active, all_done
    stopwatch = StopWatch()
    
    # Print CSV header once
    print("time_ms,heading_deg,distance_mm")
    
    while logging_active and not all_done:
        t = stopwatch.time()
        h = bob.hub.imu.heading()
        d = bob.drivebase.distance()
        # CSV row
        print(f"{t},{h},{d}")
        await wait(100)  # logging interval

def start_logging(bob: Bob):
    """Start logging in the background - call this before executing a run"""
    global logging_active, all_done
    logging_active = True
    all_done = False
    # Start logging task in background
    run_task(log_movements(bob))

def stop_logging():
    """Stop logging - call this after the run completes"""
    global logging_active, all_done
    all_done = True
    wait(200)  # Give a moment for final log entries
    logging_active = False