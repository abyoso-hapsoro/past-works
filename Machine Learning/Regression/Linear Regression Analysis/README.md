# Linear Regression Analysis
<img src="https://img.shields.io/badge/Language-Indonesian-D5AE22"> <img src="https://img.shields.io/badge/Last Update-14/06/2019-0A7BBC"> <img src="https://img.shields.io/badge/Status-Working-2CB037"> <img src="https://img.shields.io/badge/Last Test-23/06/2023-2CB037">

Applied a complete linear regression analysis on marketing dataset of media advertising budgets to sales. The data used is [marketing.rda](https://github.com/kassambara/datarium/blob/master/data/marketing.rda) and accessible with the `datarium` package.

![Import Data](https://github.com/abyoso-hapsoro/past-works/assets/51505905/e7050907-ff40-4892-b591-5634af73c1bd)

<br>
<h3 align="center">
  Data Distribution
</h3>
<p align="center">
  <img src="https://github.com/abyoso-hapsoro/past-works/assets/51505905/0c9ede02-f235-4392-9458-7f828a1e6a4b" alt="Data Distribution">
</p>

An all-feature simple linear regression model performs at an adjusted R-squared of 0.8962. At the end of the analysis, the best model given by $`\hat{y} = 6.1645 + 0.0509x_1 + 0.0352x_2 + 0.0009x_1x_2 − 0.0001x^2_1`$ improves the performance to an adjusted R-squared of 0.9857*.

(*) where $`y`$ is sales, $`x_1`$ is YouTube, $`x_2`$ is Facebook, $`x_3`$ is newspaper, and all $`x_i`$ are advertising budgets. $`x_3`$ is determined to be deteriorating to learning thus dropped. All numbers are rounded to 4 decimal points.

## Background
- Purpose: Final project for Regression Analysis (SCST603010) course taken on Year 3 Term 2
- Involvement: Individual
- Tech Stack: R

## Notes
- Planned for Improvement: No
- R Version: 3.5.3
