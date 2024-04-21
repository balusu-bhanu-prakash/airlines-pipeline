The dataset 'airlines' [obtained from [OpenML](https://www.openml.org/search?type=data&sort=runs&status=active&qualities.NumberOfInstances=between_100000_1000000&qualities.NumberOfFeatures=lte_10&id=1169)] contains 8 columns from departure airport code, arrival airport code, time, day of the week, etc.

1. Create a virtual environment (use python 3.10 or above)
   """python3 -m venv virtualenv"""
   This creates a virtual environment named 'virtualenv'. Next activate the 'virtualenv' and setup requirements and install them through 'setup.py'. Initialize git and add file names in '.gitignore' to stop tracking.

2. My datatset was intitally in ARFF format, I've processed it a bit as while its conversion to CSV format, many columns were still utf-8 encoded. After decoding was done and the duplicate records were dropped, I've saved it to the data folder.

3. Creating a source_code folder/module. This will contain all the source code files for the pipeline. Starting with exception, create an custom exception that'll be raised if anything goes wrong. This is highly helpful for debugging along with the logs. Next create a logger to log the information to debug if anything goes wrong. Add all the utiltiy type function that are called at any point to utils file.

4. Creating various componets and pipelines in the source_code folder. This involves many steps such as Data ingestion, data transformations and model training. Always include an '**init**.py' file in these folders, as these will be later used for impoorts as modules.

5. Creating & rendering HTML templates in 'app.py' flask app to locally preview the pipeline.

6. Run the training pipeline 'train_pipeline.py' to train the pipeline with various models and the input data. Once this is done, the pipeline is ready to be tested with the preprocessor and best model loaded in pickle format.(in artifacts folder)

7. Run 'app.py', which renders the HTML files and runs prediction pipeline in the background.
