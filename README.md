# Smarter Technology - Core Engineering - Challenge

---

**[Core Engineering Technical Screen](./docs/Challenge.md) requirements**

---
### Setup on Windows Environment

1. Clone this repository or open it in an online IDE or Terminal

```shell
git clone https://github.com/ovimura/SmarterTechnology-CoreEng.git
```

2. Create Python Virtual Environment running the following command on Windows system:

```shell
python -m venv venv
```

3. Execute command:

```shell
.\venv\Scripts\activate
```

---
# Smarter Technology Package Sorting Solution

### Overview
This repository contains a solution for sorting packages in Smarter Technology’s robotic automation factory. The goal is to dispatch packages to the correct stack based on their volume and mass.

- The source code for the solution can be found in the [main.py](main.py) file.

### Sorting Rules
- **Bulky**: Volume ≥ 1,000,000 cm³ or any dimension ≥ 150 cm.
- **Heavy**: Mass ≥ 20 kg.
- **Stacks**:
  - `STANDARD`: Packages that are neither bulky nor heavy.
  - `SPECIAL`: Packages that are either bulky or heavy.
  - `REJECTED`: Packages that are both bulky and heavy.

### Implementation
The function `sort(width, height, length, mass)` calculates the package volume, checks if the package is bulky or heavy, and returns the appropriate stack name (`STANDARD`, `SPECIAL`, or `REJECTED`).

```python
stack = sort(width, height, length, mass)
```

### Explanation:
  - Volume calculation: `volume = width * height * length`
  - Bulky check:
    - `volume >= 1_000_000` OR 
    - `max(width, height, length) >= 150` 
  - Heavy check: `mass >= 20`
  - Stack determination:
    - Both bulky and heavy → `REJECTED`
    - Either bulky OR heavy → `SPECIAL`
    - Otherwise → `STANDARD`

### Test Cases

The following test cases illustrate how the `sort` function handles different package scenarios:

| Width (cm) | Height (cm) | Length (cm) | Mass (kg) | Expected Stack | Description |
|------------|------------|------------|-----------|----------------|-------------|
| 50         | 50         | 50         | 10        | STANDARD       | Small package, neither bulky nor heavy |
| 200        | 50         | 50         | 10        | SPECIAL        | Bulky due to width ≥ 150 cm, but not heavy |
| 50         | 50         | 50         | 25        | SPECIAL        | Heavy (mass ≥ 20 kg), but not bulky |
| 200        | 100        | 50         | 25        | REJECTED       | Both bulky and heavy, cannot be handled automatically |
| 100        | 100        | 100        | 10        | SPECIAL        | Volume exactly 1,000,000 cm³, considered bulky |
| 150        | 20         | 20         | 19        | SPECIAL        | One dimension ≥ 150 cm, bulky, but not heavy |



#### Execute Solution:

```shell
python .\main.py
```

**Example output**: 
```
Package (50x50x50, 10kg) -> STANDARD
Package (200x50x50, 10kg) -> SPECIAL
Package (50x50x50, 25kg) -> SPECIAL
Package (200x100x50, 25kg) -> REJECTED
Package (100x100x100, 10kg) -> SPECIAL
Package (150x20x20, 19kg) -> SPECIAL
```