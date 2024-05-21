# Document-classification-HW-Scan

# Data
Assuming you have some data to test or do the inference to the model. Now preprocess the data as mentioned below

* # Mask Creation:
    1. For the mask creation, use the mask.py
    2. The inputs for the mask.py is a JSON file which we exported from the VIA tool.

        VIA TOOL: 
        It is mainly used for creating annotations using drawing around the specific regions after adding images to the project. This tool helps in annotating the objects and getting the coordinates of the objects that are annotated. The information can be exported into json or csv format.

        FLOW: Load the image >> draw boundaries >> annotate >> export to JSON.
* # Extraction and Deskew of images:
    1. Use ExtractionAndDeskew.py
* # CSV File:
    1. Generate CSV file which contains all the filenames and label.
    2. Use csvFile.py

# For the model inference, training and testing use experiment.ipynb
    1. This notebook contains all the code for the purpose of doing inference on the existing model(doc_classification.h5)(The model which is already in production in HPsmart app).
    2. We modified the existing model and stored it doc_classification_modified.keras
    3. Done inference on this model. Drawn various curves to evaluate the model.
    4. Trained the model with the available data by freezing the CNN layers and by trianing only FCN layers.
    5. After the model is trained, we saved it as doc_classification_modified_trained.keras
    6. This model is used for evaluation and we got 84% testing accuracy.

# Hyperparameter Tuning:
    * Used keras_tuner for automated hyperparameter tuning.
