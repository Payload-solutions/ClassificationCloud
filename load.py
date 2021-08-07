import json

from app.model.neuron_classification import NeuronClassification
from pprint import pprint


def test_model():
    classification = NeuronClassification(file_path="train_data/classification_data.csv",
                                          epochs_number=1000,
                                          input_shape_val=9,
                                          output_shape_val=3)
    pprint(classification.measure_predictions())


# test_model()

with open("model_training/classification_history.json", "r") as json_file:
    value = json.load(json_file)
    print(value.keys())

