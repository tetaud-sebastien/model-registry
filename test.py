from connector import MongoDBConnector
from store import store
# Example usage



# password = "5QOpq203gKyHA7YocvCP" sebastien


if __name__ == "__main__":

    username = "model"
    password = "1QUpZPL8tNTn7zVxC29e"
    host = "mongodb-3baed69e-ob7dcf057.database.cloud.ovh.net"
    db_name = "admin"
    replica_set = "replicaset"

    connector = MongoDBConnector(username, password, host, db_name, replica_set)
    client = connector.connect()
    db = client.modelDb

    # Creating or switching to demoCollection
    collection = db.demoCollection
    #first document
    document1 = {
    "outpout_dir": "models/",
    "prediction_dir": "training_inference/",
    "inputs_path": "data/data_inputs.nc",
    "target_path": "data/data_target.nc",
    "name_var_inputs": "ssh",
    "name_var_target": "ssh",
    "test_start": "2012-10-22",
    "test_end": "2012-12-02",
    "data_split": [
        90,
        10
    ],
    "train_start": "2013-01-02",
    "train_end": "2013-09-30",
    "model_architecture": "SimpleAutoencoderCNN3D",
    "depth": 6,
    "log_dir": "log",
    "loss": "MSE",
    "gpu_device": 0,
    "lr": "1e-4",
    "batch_size": 8,
    "epochs": 150,
    "workers": 8,
    "seed": 123,
    "tbp": 8888,
    "name_diag": "Diag_OSSE",
    "write_netcdf": True,
    "animate": True,
    "compute_metrics": True
    }

    # Printing the data inserted
    cursor = collection.find()
    for record in cursor:
        print(record)




    client.close()