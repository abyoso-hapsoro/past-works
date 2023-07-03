# Image Classification on Fashion-MNIST
<img src="https://img.shields.io/badge/Language-English-D5AE22"> <img src="https://img.shields.io/badge/Last Update-29/07/2019-0A7BBC"> <img src="https://img.shields.io/badge/Status-Not Working-D7624B"> <img src="https://img.shields.io/badge/Last Test-03/07/2023-2CB037">

Tasked to apply what was [learned about PyTorch](../Hands-On%20PyTorch/): "Train, Test, Validate on MLP, VGG16, ResNet-18, Resnet-50, Resnet-152" for Fashion-MNIST.

Explored further than the task required. The best performers are marked in <span style="color:yellow">yellow</span>.

| Num | Pipeline | Method | Train Accuracy | Validation Accuracy | Reference |
| :-: | -------- | ------ | :------------: | :-----------------: | --------- |
| 1 | Baseline | Multi-Layer Perceptron | 88.52% | 86.60% | <p align="center">-</p> |
| 2 | Baseline | Convolutional Neural Network | 93.29% | 90.48% | <p align="center">-</p> |
| 3 | <ul><li>Baseline</li><li>Pre-process</li></ul> | Convolutional Neural Network | 91.78% | 90.86% | <p align="center">-</p> |
| 4 | Baseline | Visual Geometry Group 16 | 95.43% | 91.53% | [VGG](https://arxiv.org/abs/1409.1556) |
| <span style="color:yellow">5</span> | <span style="color:yellow"><ul><li>Transfer Learning</li><li>Pre-process</li></ul></span> | <span style="color:yellow">Visual Geometry Group 16</span> | <span style="color:yellow">96.75%</span> | <span style="color:yellow">94.52%</span> | [VGG](https://arxiv.org/abs/1409.1556) |
| 6 | Baseline | Residual Network 18 | 98.16% | 91.38% | [ResNet](https://arxiv.org/abs/1512.03385) |
| 7 | Baseline | Residual Network 50 | 95.67% | 89.91% | [ResNet](https://arxiv.org/abs/1512.03385) |
| 8 | Baseline | Residual Network 152 | 90.62% | 87.05% | [ResNet](https://arxiv.org/abs/1512.03385) |
| 9 | <ul><li>Transfer Learning</li><li>Pre-process</li></ul> | Residual Network 18 | 96.27% | 94.10% | [ResNet](https://arxiv.org/abs/1512.03385) |
| 10 | <ul><li>Transfer Learning</li><li>Pre-process</li></ul> | AlexNet | 93.30% | 91.61% | [AlexNet](https://arxiv.org/abs/1404.5997) |
| 11 | <ul><li>Transfer Learning</li><li>Pre-process</li></ul> | SqueezeNet 1.1 | 91.99% | 91.53% | [SqueezeNet](https://arxiv.org/abs/1602.07360) |
| 12 | <ul><li>Transfer Learning</li><li>Pre-process</li></ul> | Dense Convolutional Network 121 | 96.94% | 94.21% | [DenseNet](https://arxiv.org/abs/1608.06993) |
| <span style="color:yellow">13</span> | <span style="color:yellow"><ul><li>Transfer Learning</li><li>Pre-process</li></ul></span> | <span style="color:yellow">Dense Convolutional Network 161</span> | <span style="color:yellow">97.91%</span> | <span style="color:yellow">94.51%</span> | [DenseNet](https://arxiv.org/abs/1608.06993) |
| 14 | <ul><li>Transfer Learning</li><li>Pre-process</li></ul> | Dense Convolutional Network 169 | 97.11% | 94.25% | [DenseNet](https://arxiv.org/abs/1608.06993) |
| 15 | <ul><li>Transfer Learning</li><li>Pre-process</li></ul> | GoogLeNet (Inception v1) | 95.03% | 93.57% | [GoogLeNet](https://arxiv.org/abs/1409.4842) |
| 16 | <ul><li>Transfer Learning</li><li>Pre-process</li></ul> | Mobile Net v2 | 95.09% | 93.99% | [MobileNet](https://arxiv.org/abs/1801.04381) |
| <span style="color:yellow">17</span> | <span style="color:yellow"><ul><li>Transfer Learning</li><li>Pre-process</li></ul></span> | <span style="color:yellow">ResNeXt 50</span> | <span style="color:yellow">98.18%</span> | <span style="color:yellow">94.73%</span> | [ResNeXt](https://arxiv.org/abs/1611.05431) |

<u>Pre-processing</u>: standard preprocessing (mean/std subtraction/division) and augmentation (random crops/horizontal flips)

## Background
- Purpose: AI Engineer Intern at [Konvergen AI](https://www.linkedin.com/company/konvergen-ai/)* Onboarding Project (Week 1)
- Involvement: Individual
- Tech Stack: Python, PyTorch

## Notes
- Planned for Improvement: Maybe
- Python Version: 3.6
- (*) Now [merged into Datasaur](https://www.linkedin.com/posts/datasaur_datasaureatstheworld-nlp-ocr-activity-6904289215186644992-_R4u/)