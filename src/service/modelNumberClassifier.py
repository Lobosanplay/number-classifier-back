import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.ensemble import RandomForestClassifier
import joblib

async def create_model(model_path):
    mnist = fetch_openml('mnist_784', version=1)

    X = mnist['data']
    Y = mnist['target'].astype(np.uint8)

    X_all_black = X.replace([range(1,255)], 255)

    rnd_clf = RandomForestClassifier(n_estimators=500, max_leaf_nodes=16, n_jobs=-1)
    rnd_clf.fit(X_all_black.values, Y)

    joblib.dump(rnd_clf, model_path)
    return 'entrenamiento de el modelo terminado....'
