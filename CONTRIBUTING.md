# Contributing to The Tinikling Method

Thank you for helping us advance the future of sports science and rhythm athletics. By contributing to this repository, you help optimize elite coordination tracking for field and court athletes worldwide.

## 1. Code of Conduct & IP Boundaries
Please remember that all algorithmic additions, configurations, and performance data models submitted to this project fall strictly under our master licensing architecture. By opening a Pull Request, you certify that your contribution is your original work and does not violate any external intellectual property agreements.

## 2. Technical Submission Guidelines
To keep our code highly stable and ready for the NVIDIA Inception pipeline, all additions must meet these requirements:
* **Mathematical Grounding:** Any new multi-sport analytics additions must be accompanied by explicit biomechanical formulas backed by sports-science consensus.
* **Comprehensive Testing:** All pipeline updates require matching test logic additions inside the `tests/` directory.
* **Efficiency Standards:** Code must optimize data matrices using vectorized NumPy methods. Avoid heavy computational nested loops that could induce processing lag on Edge devices (NVIDIA Jetson).

## 3. Pull Request Protocol
1. Fork the repository and build your feature branch out from `main`.
2. Run your validation scripts locally using `pytest tests/` to confirm all validation arrays pass cleanly.
3. Submit your PR with a thorough explanation of the sports science metric or configuration parameter you are updating.
