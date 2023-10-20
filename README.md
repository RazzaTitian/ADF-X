# ADF-X (Advanced Data Factory - eXperimental)

## Overview
ADF-X is an ambitious, groundbreaking project designed to create a highly modular, robust, and complex data generation factory. The primary objective is to produce synthetic data that can fulfil all possible variations, ensuring the data is as accurate and comprehensive as possible. ADF-X is not just a data generator; it's a complete data ecosystem tailored to be highly customizable, allowing users to specify the type of data they need, the number of iterations, and the expected amount of data.

## Components

### Admin AI
The Admin AI serves as the factory's starting point and user-friendly interface. It inquires about the user's specific needs, such as the phase for which the data is needed, the number of iterations, and the expected amount of data, thereby determining the course of action for the factory.

### OldData and OriginalData
Two mutable copies of the original dataset serve as the basis for data generation. `OldData` is actively worked upon for data generation, while `OriginalData` serves as a preserved reference copy.

### Rooms
The factory is divided into multiple "Rooms," each with a unique combination of data generation algorithms. These algorithms range from Simple Random Sampling, SMOTE, Gaussian Mixture Models, Monte Carlo Simulation, Rule-Based Generation, Data Perturbation to advanced machine learning models like GANs and VAEs.

#### Room 1
- All Algorithms + Simple VAE

#### Room 2
- All Algorithms + Simple GAN

#### Room 3
- All Algorithms + Simple VAE + Simple GAN

#### Room 4
- All Algorithms (No VAE or GAN)

### Post-Processing
After the data is generated in each Room, it undergoes refinement using complex GANs and VAEs versions. The data from each room is then combined into a final, highly nuanced, and accurate dataset.

## Workflow

1. **Admin Inquiry**: Determine user needs.
2. **Data Import**: Import preprocessed datasets for different phases.
3. **Room Processing**: Data is sent to Rooms based on user input.
4. **Post-Processing**: Further refinement of generated data.
5. **Output**: The final dataset meets the user's specifications.

## Usage
The factory is designed to be highly modular and customizable. Users can easily plug in different algorithms, adjust parameters, and add new "Rooms" as needed.

## Target
The ultimate aim of ADF-X is to be a one-stop solution for all data generation needs, whether for academic research, business analytics, or machine learning projects. It strives to produce a synthetic dataset that is not just large in volume but also rich in quality, ensuring that all possible data variations are covered.

## Glossary of Terms and Abbreviations

### General Terms

- **ADF-X**: Advanced Data Factory - eXperimental. The name of the project.
- **Admin AI**: The AI interface that interacts with the user to determine the specifications for data generation.
- **OldData**: A mutable copy of the original dataset used for data generation.
- **OriginalData**: A preserved copy of the original dataset for reference.
- **Room**: A section of the factory responsible for data generation using a specific set of algorithms.
- **Post-Processing**: The steps to refine the generated data after a Room has produced it.

### Rooms

- **Room 1**: Utilizes all algorithms plus a Simple VAE for data generation.
- **Room 2**: Utilizes all algorithms plus a Simple GAN for data generation.
- **Room 3**: Utilizes all algorithms plus Simple VAE and Simple GAN for data generation.
- **Room 4**: Utilizes all algorithms except VAE and GAN for data generation.

### Algorithms and Models

- **VAE**: Variational Autoencoder. A type of generative model.
- **GAN**: Generative Adversarial Network. Another type of generative model.
- **Simple Random Sampling**: A basic method for generating new data points by randomly sampling from the existing data.
- **SMOTE**: Synthetic Minority Over-sampling Technique. Used for balancing classes in the dataset.
- **Gaussian Mixture Models**: Used for generating new data points based on Gaussian distribution.
- **Monte Carlo Simulation**: A statistical method for predicting different outcomes' probability.
- **Rule-Based Generation**: Generates new data points based on predefined rules.
- **Data Perturbation**: Adds noise to existing data points to generate new data.


Copyright © Muhammad Razza Titian Jiwani 2023

All rights reserved. This project and its associated code, assets, and documentation are protected by copyright law. No part of this project may be reproduced, distributed, or transmitted in any form or by any means, including photocopying, recording, or other electronic or mechanical methods, without the prior written permission of the copyright owner, Muhammad Razza Titian Jiwani, except in the case of brief quotations embodied in critical reviews and certain other noncommercial uses permitted by copyright law.

This project is not open-sourced, and no license or permission is granted for its use, modification, or distribution. Any unauthorized use, reproduction, or distribution of this project or its components is strictly prohibited and will be considered a violation of copyright law, subject to legal action, including but not limited to fines, injunctions, and/or criminal charges.

Commercial use of this project, in whole or in part, is expressly forbidden. Any inquiries regarding commercial use or licensing should be directed to zeusprototype01@gmail.com.

All rights, including but not limited to intellectual property rights, remain the exclusive property of Muhammad Razza Titian Jiwani.

For questions or inquiries, please contact:

email: zeusprototype01@gmail.com

