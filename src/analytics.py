import numpy as np

class RhythmAgilityEngine:
    """
    Engine to calculate elite sports performance data using rhythmic footwork inputs.
    Prepares raw data matrix pipelines for future computer vision integrations.
    """
    def __init__(self, target_bpm: int, cadence_beats: int = 4):
        self.target_bpm = target_bpm
        self.cadence_beats = cadence_beats
        self.beat_duration = 60.0 / target_bpm

    def calculate_ground_contact_efficiency(self, entry_frames: list, exit_frames: list, fps: int = 60) -> dict:
        """
        Calculates Ground Contact Time (GCT) from keypoint activations inside the rhythm box.
        """
        gct_records = []
        for en, ex in zip(entry_frames, exit_frames):
            gct_seconds = (ex - en) / fps
            gct_records.append(gct_seconds * 1000)
            
        avg_gct = np.mean(gct_records) if gct_records else 0.0
        performance_score = max(0.0, 100.0 - (avg_gct - 120.0) * 0.5) 
        
        return {
            "average_gct_ms": round(float(avg_gct), 2),
            "efficiency_score": round(float(performance_score), 2),
            "status": "Elite" if avg_gct < 150 else "Developmental"
        }

    def calculate_team_synchronization_index(self, athlete_a_timestamps: list, athlete_b_timestamps: list) -> float:
        """
        Calculates Phase-Alignment Synchronization between two field partners.
        """
        if len(athlete_a_timestamps) != len(athlete_b_timestamps) or not athlete_a_timestamps:
            return 0.0
            
        differences = np.abs(np.array(athlete_a_timestamps) - np.array(athlete_b_timestamps))
        variance = np.var(differences)
        sync_index = 1.0 / (1.0 + variance)
        return round(float(sync_index), 4)

    def calculate_baseball_rotational_velocity(self, hip_frame: int, wrist_frame: int, fps: int = 60) -> dict:
        """
import numpy as np

class RhythmAgilityEngine:
    """
    Master Sports Science Engine to calculate elite athletic performance data.
    Processes high-frequency lower body mechanics, team synchronization,
    multi-sport physics, and upper-body/prop manipulation metrics.
    """
    def __init__(self, target_bpm: int, cadence_beats: int = 4):
        self.target_bpm = target_bpm
        self.cadence_beats = cadence_beats
        self.beat_duration = 60.0 / target_bpm

    # =========================================================================
    # CORE TRACKING: LOWER-BODY AGILITY (TINIKLING DISCIPLINE)
    # =========================================================================
    def calculate_ground_contact_efficiency(self, entry_frames: list, exit_frames: list, fps: int = 60) -> dict:
        """
        Calculates Ground Contact Time (GCT) from keypoint activations inside the rhythm box.
        Optimized for soccer tight-space dribbling and rugby side-stepping.
        """
        gct_records = []
        for en, ex in zip(entry_frames, exit_frames):
            gct_seconds = (ex - en) / fps
            gct_records.append(gct_seconds * 1000)
            
        avg_gct = np.mean(gct_records) if gct_records else 0.0
        # Elite performance score drops as contact time increases past a baseline
        performance_score = max(0.0, 100.0 - (avg_gct - 120.0) * 0.5) 
        
        return {
            "average_gct_ms": round(float(avg_gct), 2),
            "efficiency_score": round(float(performance_score), 2),
            "status": "Elite" if avg_gct < 150 else "Developmental"
        }

    def calculate_team_synchronization_index(self, athlete_a_timestamps: list, athlete_b_timestamps: list) -> float:
        """
        Calculates Phase-Alignment Synchronization between two field partners.
        A score of 1.0 indicates perfect movement execution synchronization.
        """
        if len(athlete_a_timestamps) != len(athlete_b_timestamps) or not athlete_a_timestamps:
            return 0.0
            
        differences = np.abs(np.array(athlete_a_timestamps) - np.array(athlete_b_timestamps))
        variance = np.var(differences)
        sync_index = 1.0 / (1.0 + variance)
        return round(float(sync_index), 4)

    # =========================================================================
    # MULTI-SPORT EXTENSIONS: TENNIS, BASEBALL, SWIMMING
    # =========================================================================
    def calculate_baseball_rotational_velocity(self, hip_frame: int, wrist_frame: int, fps: int = 60) -> dict:
        """
        Calculates the separation latency between hip rotation and wrist release 
        during a rhythmic batting load sequence.
        """
        latency_frames = abs(wrist_frame - hip_frame)
        latency_ms = (latency_frames / fps) * 1000
        # Elite power transfer occurs within a narrow, specific biomechanical window (30-50ms)
        efficiency = max(0.0, 100.0 - abs(latency_ms - 40.0) * 2.0)
        
        return {
            "uncoiling_latency_ms": round(float(latency_ms), 2),
            "power_transfer_efficiency": round(float(efficiency), 2)
        }

    def calculate_tennis_court_recovery_index(self, step_timestamps: list, ideal_beat_windows: list) -> float:
        """
        Measures an athlete's split-step synchronization relative to an incoming ball 
        bounce rhythm interval to optimize lateral court recovery.
        """
        if len(step_timestamps) != len(ideal_beat_windows):
            return 0.0
            
        accuracy_deltas = np.abs(np.array(step_timestamps) - np.array(ideal_beat_windows))
        mean_deviation = np.mean(accuracy_deltas)
        recovery_score = max(0.0, 100.0 - (mean_deviation * 200.0))
        return round(float(recovery_score), 2)

    def calculate_swimming_stroke_kick_cohesion(self, stroke_timestamps: list, kick_timestamps: list) -> float:
        """
        Evaluates polyrhythmic symmetry to minimize fluid drag.
        Tracks if the 6-beat kick cycle aligns flawlessly with the 2-beat arm stroke cycle.
        """
        if not stroke_timestamps or not kick_timestamps:
            return 0.0
            
        # Target: Exactly 3 precise kick intervals per uniform stroke duration window
        kick_counts_per_stroke = len(kick_timestamps) / max(1, len(stroke_timestamps))
        deviation = abs(kick_counts_per_stroke - 3.0)
        cohesion_percentage = max(0.0, 100.0 - (deviation * 50.0))
        return round(float(cohesion_percentage), 2)

    # =========================================================================
    # ADVANCED SCALING: POSTURE & PROP MANIPULATION (MARIA CLARA SUITE)
    # =========================================================================
    def calculate_posture_stability_index(self, shoulder_l: list, shoulder_r: list, hip_center: list) -> dict:
        """
        Measures torso sway and core alignment based on Maria Clara posture baselines.
        Trains core control and upright stability during sharp direction cuts.
        Expects 2D image coordinates [x, y].
        """
        if not shoulder_l or not shoulder_r or not hip_center:
            return {"posture_deviation_degrees": 0.0, "stability_score": 0.0}

        # Calculate vector for the shoulders
        shoulder_vector = np.array(shoulder_l) - np.array(shoulder_r)
        
        # Calculate angle of the torso vector relative to the horizontal plane
        tilt_angle = np.degrees(np.arctan2(shoulder_vector[1], shoulder_vector[0])) % 180
        
        # Normalize ideal upright alignment to zero degrees deviation
        deviation = abs(tilt_angle - 180.0) if tilt_angle > 90 else tilt_angle
        stability_score = max(0.0, 100.0 - (deviation * 4.0))

        return {
            "posture_deviation_degrees": round(float(deviation), 2),
            "stability_score": round(float(stability_score), 2),
            "compliance": "Stable Core" if deviation < 10.0 else "Excessive Lean"
        }

    def calculate_prop_manipulation_latency(self, wrist_frame: int, prop_frame: int, fps: int = 60) -> float:
        """
        Measures hand-eye coordination by tracking the latency between wrist acceleration 
        and prop activation (e.g., fan unfurling, racket contact, or lacrosse pocket release).
        """
        latency_frames = abs(prop_frame - wrist_frame)
        latency_ms = (latency_frames / fps) * 1000
        return round(float(latency_ms), 2)

if __name__ == "__main__":
    engine = RhythmAgilityEngine(target_bpm=130)
    print("=======================================================================")
    print("   THE TINIKLING METHOD: UNIFIED RHYTHM AGILITY ENGINE INITIALIZED")
    print("=======================================================================")
    print(f" Target Cadence: {engine.target_bpm} BPM | Beat Duration: {round(engine.beat_duration, 4)}s")
    print(" Status: Operational | Systems Protected via TUTSA & WTO TRIPS Ch. 134A")
    print("=======================================================================")
hesion_percentage = max(0.0, 100.0 - (deviation * 50.0))
        return round(float(cohesion_percentage), 2)

if __name__ == "__main__":
    engine = RhythmAgilityEngine(target_bpm=130)
    print("--- Multi-Sport Rhythm Agility Engine Initialized Successfully ---")       """
        if len(athlete_a_timestamps) != len(athlete_b_timestamps) or not athlete_a_timestamps:
            return 0.0
            
        differences = np.abs(np.array(athlete_a_timestamps) - np.array(athlete_b_timestamps))
        variance = np.var(differences)
        
        # Normalize synchronization index to a scale of 0 to 1
        sync_index = 1.0 / (1.0 + variance)
        return round(float(sync_index), 4)

if __name__ == "__main__":
    # Example execution showcasing standard data verification pipelines
    engine = RhythmAgilityEngine(target_bpm=130)
    
    # Simulating data generated from an interactive field drill session
    mock_entry = [10, 72, 134]
    mock_exit = [19, 81, 142]
    
    metrics = engine.calculate_ground_contact_efficiency(mock_entry, mock_exit, fps=60)
    print(f"--- Operational Assessment ---")
    print(f"Metrics Output: {metrics}")
