# Machine Learning Ready Data (MLRD)

![A Mallard in the water](mallard.jpg)

## Introduction

Geospatial models are defined by their ability to answer a specific question based on two inputs: when and where. For example, how many cars are in the parking lot at the Walmart located at 123 Main Street at 11:42 AM on August 1st, 2023? Or another: how many hectares of wheat crops are being grown within the Bavarian region of Germany in June of 2022?

Ideally, we should be able to find a machine learning model that answers the question we have, feed it the when (single date-time or range of date-times) and where (geometry), and receive the answer in an actionable format (classification raster, single value, etc.). In practice, however, this is a challenging and time-consuming task. 

Geospatial machine learning models are often built without inferencing in mind and require a user to find the imagery themselves, pre-process the imagery in the same way that the imagery the model was trained on was pre-processed, run the inference on the pre-processed imagery, and post-process the model's inferences.

The goal of the Machine Learning Ready Data (MLRD: pronounced Mallard) specification is to produce a standardized container for geospatial machine learning training data which enables the creation of models that are easy to finetune and inference on.


## Problems

### 1) Bulk of Imagery in Training Datasets

Geospatial machine learning training datasets typically consist of label files (GeoTIFF, GeoJSON) and matching imagery (Sentinel-2, Sentinel-1, Landsat-8). Imagery is downloaded from the source, pre-processed (normalized, chipped, renamed), and packaged with the labels as a "completed" training dataset. Given the nature of geospatial data, this training dataset can quickly become unwieldy. A "small" training dataset of a few hundred samples can be multiple gigabytes while large training datasets are multiple terabytes. The bulk of these packages come from the imagery rather than the actual labels.

### 2) Pre-processing of Imagery

Geospatial machine learning models depend on imagery to run inferences. Imagery usually requires some level of pre-processing before being fed into a machine learning model. The code required to pre-process the imagery isn't always provided alongside the model code and if it is,  you will need to process your imagery before you run the model inferencing.


## Solutions

### 1) Don't Package Imagery, Package Context

Training datasets should only contain the labels for the task and enough context to programmatically locate the matching imagery. Context should be provided in the form of a STAC catalog which links labels to imagery cataloged within other STAC catalogs.

### 2) MLRD Model Interfaces

Model code should have two interfaces: one which trains and finetunes the model weights, and another which runs inferences. The training and finetuning interface should take a MLRD training dataset catalog as an input, load the label data, load (locate, download, transform) the linked imagery, and train the model. The inferencing interface should take in a date-time (or date-time range) and geometry, load (locate, download, transform) the imagery required for inferencing from the model's sources, and returned the inferencing result.

## Envisioning an Ecosystem of Tools

Standardizing the format of geospatial machine learning training datasets and models enables the creation of a new ecosystem of tools similar to the ecosystem of tools created by the standardization of Spatio-Temporal metadata with STAC. The following are just a few examples of tools which could be created and interoperable if MLRD becomes adopted:

* Labeling platform where a user selects an imagery source, let's say Sentinel-1, defines their area of interest and the dimensions of a single sample, and begins classifying samples. At the end of the classification a user exports a small and portable packaged MLRD training dataset.
* Validation tool where a user can input a packaged MLRD training dataset and receive a response of whether the training dataset is valid or invalid according to the MLRD specification.
* Python framework for providing the training/finetuning and inferencing interfaces for a model, allowing machine-learning engineers to focus only on the model itself.
* Inferencing APIs for models where a user makes a `POST` request to an API endpoint with a date-time and geometry and receives the model inference as a result.
