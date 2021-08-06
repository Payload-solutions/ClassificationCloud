from app.model.neuron_classification import NeuronClassification




def test_model():
    classification = NeuronClassification(file_path="train_data/classification_data.csv", 
                                        epochs_number=1000, 
                                        input_shape_val=9, 
                                        output_shape_val=3)