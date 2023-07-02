# An Attempt to Generalize the Edge Irregularity Strength of m × n × l Grid Graphs
<img src="https://img.shields.io/badge/Language-Mixed-D5AE22"> <img src="https://img.shields.io/badge/Last Update-13/02/2019-0A7BBC"> <img src="https://img.shields.io/badge/Status-Not Tested-D7624B">

This project was an attempt to solve the open problem:
<p align="center">
    Determine the exact value of $es(P_n\Box P_m\Box P_l)$ for $m,n\geq2$ and $l\geq3$
</p>

posed in July 2018 at AKCE International Journal of Graphs and Combinatorics, available [here](https://www.sciencedirect.com/science/article/pii/S097286001730107X). Checking back in July 2023, this problem doesn't seem to have been solved yet*.

## Preliminaries
1. Definition of Graph Cartesian Product
<p align="center">
    <img src="https://github.com/abyoso-hapsoro/past-works/assets/51505905/1b47f984-0d44-47c2-8c8f-07ab3e3610db" width="600" alt="Domino Graph">
</p>

2. Example of $m\times n\times l$ Grid Graph with $m=n=l=2$, a.k.a the Cubical Graph $Q_3$
<p align="center">
    <img src="https://github.com/abyoso-hapsoro/past-works/assets/51505905/ae34f338-19d1-4580-9f53-27281985db04" width="600" alt="Q3">
</p>

3. Edge Irregularity Strength of $m\times n\times l$ Grid Graph
<p align="center">
    <img src="https://github.com/abyoso-hapsoro/past-works/assets/51505905/1c643fdb-3e1a-4fa3-a2dc-f463a7b27e7e" width="450" alt="Edge Irregularity Strength">
</p>

4. Edge Irregular Labeling of the Cubical Graph $Q_3$
<p align="center">
    <img src="https://github.com/abyoso-hapsoro/past-works/assets/51505905/6de98581-43b0-4d56-a811-6c3235104a27" width="300" alt="Q3 Labeling">
</p>

## Our Results
1. Lower Bound Theorem for Edge Irregularity Strength of the $m\times n\times l$ Grid Graph
<br>The proof for our theorem is presented in page 5 of [Paper.pdf](Paper.pdf).
<p align="center">
    <img src="https://github.com/abyoso-hapsoro/past-works/assets/51505905/0d55ae15-e906-48fa-9a64-225e630e0172" width="600" alt="Our Theorem">
</p>

2. Conjecture to the Open Problem
<br>We believe that the Edge Irregularity Strength of $P_n\Box P_m\Box P_l$ where $m,n,l\geq2$ is exactly the lower bound of our theorem. However, we have yet to prove this.
<p align="center">
    <img src="https://github.com/abyoso-hapsoro/past-works/assets/51505905/ef985b05-fd2e-4145-a64b-978c0e372750" width="600" alt="Our Conjecture">
</p>

## Exploring the Cubical Graph $Q_4$
As an alternative to proving, we explore an edge irregular labeling of $Q_4=P_3\Box P_3\Box P_3$ to test our conjecture.
<p align="center">
    <img src="https://github.com/abyoso-hapsoro/past-works/assets/51505905/e5d80696-8166-4af6-903d-7fc3f0d7f431" width="600" alt="Q4">
</p>
<p align="center">
    <img src="https://github.com/abyoso-hapsoro/past-works/assets/51505905/a119e62e-a0b4-4136-9449-9a83711d2af5" width="600" alt="Q4 Labeling">
</p>
The edge weight 34 is missing implying the existence of a better configuration. This hints our conjecture being correct for this specific case.

## Background
- Purpose: Final project for Graph Theory (SCMA603162) course taken on Year 3 Term 1
- Involvement: Team
    - Team Size: 4
- Tech Stack: LaTeX

## Notes
- Planned for Improvement: No
- (*) From own searching, there is a good possibility this is inaccurate
