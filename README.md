# Lung Cancer Detection

## INTRODUCTION

Lung cancer is the leading cause of cancer deaths, and symptoms usually don't appear until the disease is advanced, causing delay in diagnosis. To address this problem, a double scan method is proposed to determine the exact condition and predict the spread of cancer. An AI-based 3D model of lungs is being developed using CT scans, which detects and highlights cancerous clots, making it easier for doctors to diagnose. The model is being built using datasets from LUNA16 and Cancer Imaging Archive, and preprocessing methods are applied to ensure the data is easier for the model building process. The process involves several steps using different tools, such as 2D to 3D converter, model and segment calculations, and comparison between images before and after conversion. The end result is a low poly object that can be used to enhance 3D models with edit segments, resulting, and trimming.

## OBJECTIVES
### Data Extraction: 
  Getting a Partial Amount of CT scans from the LUNA16 Dataset
considering its entire size. It comes in the form of a .raw file and a .mhd file. The raw file
holds the scans, while the mhd file is the metadata to the raw file.

### Data Pre-processing: 
The CT scans go through feature engineering and necessary features
are selected for the training process to avoid overfitting the model by masking the nodules
and extracting the lungs alone from the original image. This gives us the only features that
matter. We separate the training, validation and test sets in 98:1:1 ratio respectively. Noise
removal and Image Enhancement will be done depending on the effect on data.

### Model Training: 
This project mainly uses U-Net architecture to train the model which is
commonly used in segmentation of bio-medical images. The hyper-parameters are changed
to make the model generalize to the validation. While different models using different
architectures are also trained along. The trained models are saved in .h5 form.

### Model Evaluation: 
The models are evaluated with the validation and test sets individually
with respect to their True Positive, True Negative, False Positive, False Negative and Mean
Dice Co-efficient values. Then, the metrics are compared between the different models and
the best generalized model is chosen.

### Deploying The Model: 
To deploy the model into real world, we use Flask web framework to
build the backend of the website. It is integrated with TensorFlow and the frontend of the
website. The website takes both the. mhd and .raw file and it is processed through the saved
final model and the predicted result is shown.

![image](https://user-images.githubusercontent.com/54493809/236686018-a9e9a4be-2c88-486a-9492-9233b92601e6.png)


## SUMMARY
The main goal of our project is to find out the Exact condition of cancer clots in a patients’ lungs
using the double scan method to find the exact condition of the cancer in the patient body and we
can also predict the rate of spreading the cancer by this we can overcome the above problems. And
to make it a bit accessible we are making an 3d AI based model of lungs using CT scans which
detects and highlights the area of cancer clots.
