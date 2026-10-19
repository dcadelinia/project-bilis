import pytest
from src.analytics import RhythmAgilityEngine

@pytest.fixture
def engine():
    # Initialize a baseline 120 BPM engine for standard athletic testing
    return RhythmAgilityEngine(target_bpm=120)

def test_ground_contact_efficiency_elite(engine):
    # Simulate an elite soccer player with rapid 133ms ground contact times
    entry = [10, 20, 30]
    exit_frames = [18, 28, 38]  # 8 frames at 60fps = ~133.3ms
    
    result = engine.calculate_ground_contact_efficiency(entry, exit_frames, fps=60)
    assert result["status"] == "Elite"
    assert result["average_gct_ms"] == 133.33
    assert result["efficiency_score"] > 90.0

def test_team_synchronization_index_perfect(engine):
    # Simulate two rugby defenders moving perfectly in sync
    athlete_a = [1.0, 2.0, 3.0]
    athlete_b = [1.0, 2.0, 3.0]
    
    sync_score = engine.calculate_team_synchronization_index(athlete_a, athlete_b)
    assert sync_score == 1.0

def test_baseball_rotational_velocity(engine):
    # Simulate a baseball batter hitting an optimal 40ms kinetic uncoiling window
    hip_frame = 10
    wrist_frame = 12  # 2 frames at 50fps = 40ms
    
    result = engine.calculate_baseball_rotational_velocity(hip_frame, wrist_frame, fps=50)
    assert result["uncoiling_latency_ms"] == 40.0
    assert result["power_transfer_efficiency"] == 100.0

def test_swimming_stroke_kick_cohesion_ideal(engine):
    # Simulate a perfect 3:1 ratio (6-beat kick cycle relative to a 2-stroke block)
    strokes = [1, 2]
    kicks = [1, 2, 3, 4, 5, 6]
    
    cohesion = engine.calculate_swimming_stroke_kick_cohesion(strokes, kicks)
    assert cohesion == 100.0
